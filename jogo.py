import pyxel
import coronajogador as cj
import obst as obs
import fundo
from random import randint
posY = [0, 16, 32, 48, 64] #Posições fixas do Y
dist = [60, 50, 40, 35, 30, 25, 20, 15] #Distâncias entre os obstáculos
dif = len(dist) #Dificuldade relacionada a distância

class Jogo:
    player = cj.Coronajogador(0, 0)
    objetos = []
    contframes = 0
    width = 0
    height = 0
    status = "PERDEU"
    fundos = []
    animplayer = 0
    count = 0
    def __init__(self, w, h):
        self.player.x = 20
        self.player.y = 25
        self.player.estado(True)
        self.width = w
        self.height = h
        self.status = "JOGANDO"
        self.pontos = 0
        self.dif = 0            #Dificuldade relacionada a distância
        self.av = False         #Avançar o nível de dificuldade
        for i in self.objetos:
            i.setX(180)
        a = fundo.Fundo(0,0,180,80,0)
        self.fundos.append(a)

    def update(self):
        pyxel.mouse(False)
        self.mouse()
        self.contframes += 1
        if (self.av & (self.dif<dif)):
            self.av = False
            self.dif += 1
            #print("Avançou para {}".format(str(self.dif))

    # ----------------------------- SETANDO OBSTÁCULOS --------------------------------
        if self.contframes >= dist[self.dif]:
            self.contframes = 0
            obj = obs.Obstaculos(self.status, posY[randint(0, 4)], randint(0,7))
            obj.setX(180)
            self.objetos.append(obj)
            #print("Tenho {} objetos".format(len(self.objetos)))

    # -------------------------- CONFIGURAÇÃO DO JOGADOR -------------------------------
        self.player.update()
        #if self.player.update() == 1:
            #self.animplayer = 1

    # ------------------------ CONFIGURAÇÃO DOS OBSTÁCULOS -----------------------------
        for o in self.objetos:
            o.update()
        for i in range(len(self.objetos)):
            if self.objetos[i].obsX < 4:
                self.pontos += 5 + self.dif   # Pontuação fixa + nível de dificuldade
                del(self.objetos[i])
                break

    # ------------------------ CONFIGURAÇÃO DE COLISÕES --------------------------------
        for i in self.objetos:
            if self.player.x > i.obsX and self.player.x <= i.obsX+16:
                if self.player.y > i.obsY and self.player.y <= i.obsY+16:
                    self.player.estado(False)
                    for j in range(len(self.objetos)):
                        self.objetos[j].setState("PERDEU")
                    break
            else:
                for j in range(len(self.objetos)):
                        self.objetos[j].setState("JOGANDO")

    # -------------------------- CONFIGURAÇÃO DO FUNDO ---------------------------------
        for i in range(len(self.fundos)):
            if self.fundos[i].x + self.fundos[i].w == 180:
                if self.fundos[i].tipo < 3:
                    a = fundo.Fundo(181,0,180,80,self.fundos[i].tipo+1)
                    self.fundos.append(a)
                else:
                    a = fundo.Fundo(181,0,180,80,0)
                    self.fundos.append(a)
                    # Quando volta pra China
                    if (self.dif < dif): # Avançar nível de dificuldade
                        self.av = True
            if self.fundos[i].x + self.fundos[i].w <= 0:
                del(self.fundos[i])
                break
            self.fundos[i].update()

    def draw(self):
        pyxel.cls(10)
        for i in self.fundos:
            i.draw()
        for i in self.objetos:
            i.draw()
        pyxel.text(2, 72, f"Pontos {self.pontos}", 10)
        if self.animplayer == 1:
            self.count += 1
        if self.count >= 10:
            self.count = 0
            self.animplayer = 0
        self.player.draw(self.animplayer)

    
    def mouse(self):
        if pyxel.btn(pyxel.KEY_ENTER):
            return [True, 0]
        if self.player.vivo == False:
            return[True, 1, self.pontos]
        return [False]
    
    def reset(self):
        self.player.x = 20
        self.player.y = 25
        self.pontos = 0
        self.objetos = []
        self.contframes = 0
        self.animplayer = 0
        self.count = 0
        self.dif = 0
        self.av = False