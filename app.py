import pyxel
import menuIniciar as mi
import menuPausa as mp
import jogo as j
import creditos as c
import gameover as go

class App:
    stat = "MENU"         #estados possiveis: "MENU"; "PAUSA"; "JOGO"; "CREDITOS"; "GAMEOVER";
    status = [mi.Iniciar(180, 80), mp.Pause(180, 80), j.Jogo(180, 80), c.Creditos(180, 80), go.GameOver(180, 80)]
    width = 0
    height = 0
    sound = True
    soundChange = True
    pontos = 0
    estadoJogador = True
    def __init__(self, w, h):
        self.width = w
        self.height = h
        pyxel.init(self.width, self.height)
        pyxel.load("assets/menu.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if self.soundChange == True:
            self.play_music()

        self.mudaEstado()

        if self.stat == "MENU":
            self.status[0].update()
        elif self.stat == "PAUSA":
            self.status[1].update()
        elif self.stat == "JOGO":
            self.status[2].update()
        elif self.stat == "CREDITOS":
            self.status[3].update()
        elif self.stat == "GAMEOVER":
            self.status[4].update()
        self.status[4].setPontos(self.pontos)

    def draw(self):
        pyxel.cls(3)
        if self.stat == "MENU":
            self.status[0].draw()
        elif self.stat == "PAUSA":
            self.status[1].draw()
        elif self.stat == "JOGO":
            self.status[2].draw()
        elif self.stat == "CREDITOS":
            self.status[3].draw()
        elif self.stat == "GAMEOVER":
            self.status[4].draw()
    
    def mudaEstado(self):
        if self.stat == "MENU":
            prox = self.status[0].mouse()
            if prox[0] == True:
                if prox[1] == 0: #Música ON
                    self.sound = True
                    self.soundChange = True
                elif prox[1] == 1: #Música OFF
                    self.sound = False
                    self.soundChange = True
                elif prox[1] == 2: #Creditos
                    self.stat = "CREDITOS"
                    self.soundChange = True
                elif prox[1] == 3: #Iniciar
                    self.status[2].reset()
                    self.stat = "JOGO"
                    self.soundChange = True
        
        elif self.stat == "PAUSA":
            prox = self.status[1].mouse()
            if prox[0] == True:
                if prox[1] == 0: #Música ON
                    self.sound = True
                    self.soundChange = True
                elif prox[1] == 1: #Música OFF
                    self.sound = False
                    self.soundChange = True
                elif prox[1] == 2: #JOGAR
                    self.stat = "JOGO"
                    self.soundChange = True
                elif prox[1] == 3: #SAIR
                    self.stat = "MENU"
                    self.soundChange = True
        
        elif self.stat == "JOGO":
            prox = self.status[2].mouse()
            if prox[0] == True:
                if prox[1] == 0: #VOLTAR
                    self.stat = "PAUSA"
                    self.soundChange = True
                elif prox[1] == 1:
                    self.stat = "GAMEOVER"
                    self.soundChange = True
                    self.pontos = prox[2]
        
        elif self.stat == "CREDITOS":
            prox = self.status[3].mouse()
            if prox[0] == True:
                if prox[1] == 0: #VOLTAR
                    self.stat = "MENU"
                    self.soundChange = True
        
        elif self.stat == "GAMEOVER":
            prox = self.status[4].mouse()
            if prox[0] == True:
                if prox[1] == 0: #Música ON
                    self.sound = True
                    self.soundChange = True
                elif prox[1] == 1: #Música OFF
                    self.sound = False
                    self.soundChange = True
                elif prox[1] == 2: #JOGO
                    self.status[2].reset()
                    self.stat = "JOGO"
                    self.soundChange = True
                elif prox[1] == 2: #SAIR
                    self.stat = "MENU"
                    self.soundChange = True
    

    def play_music(self):
        if self.sound == True:
            if self.stat == "MENU" or self.stat == "PAUSA" or self.stat == "CREDITOS":
                pyxel.play(1, 0, loop=True)
            if self.stat == "JOGO":
                pyxel.play(1, 2, loop=True)
            if self.stat == "GAMEOVER":
                pyxel.play(1, 3, loop=True)
        else:
            pyxel.stop(1)
        self.soundChange = False

App(180, 80)