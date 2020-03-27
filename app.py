import pyxel
import menuIniciar as mi
import menuPausa as mp
import jogo as j
import creditos as c

class App:
    stat = "JOGO"         #estados possiveis: "MENU"; "PAUSA"; "JOGO"; "CREDITOS";
    status = [mi.Iniciar(180, 80), mp.Pause(180, 80), j.Jogo(180, 80), c.Creditos(180, 80)]
    width = 0
    height = 0
    def __init__(self, w, h):
        self.width = w
        self.height = h
        pyxel.init(self.width, self.height)
        #pyxel.load("assets/BReCHN.pyxres")
        pyxel.load("assets/menu.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        self.mudaEstado()

        if self.stat == "MENU":
            self.status[0].update()
        elif self.stat == "PAUSA":
            self.status[1].update()
        elif self.stat == "JOGO":
            self.status[2].update()
        elif self.stat == "CREDITOS":
            self.status[3].update()

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
    
    def mudaEstado(self):
        if self.stat == "MENU":
            prox = self.status[0].mouse()
            if prox[0] == True:
                if prox[1] == 0: #Música ON
                    pass
                elif prox[1] == 1: #Música OFF
                    pass
                elif prox[1] == 2: #Creditos
                    self.stat = "CREDITOS"
                elif prox[1] == 3: #Iniciar
                    self.stat = "JOGO"
        
        elif self.stat == "PAUSA":
            prox = self.status[1].mouse()
            if prox[0] == True:
                if prox[1] == 0: #Música ON
                    pass
                elif prox[1] == 1: #Música OFF
                    pass
                elif prox[1] == 2: #JOGAR
                    self.stat = "JOGO"
                elif prox[1] == 3: #SAIR
                    self.stat = "MENU"
        
        elif self.stat == "JOGO":
            prox = self.status[2].mouse()
            if prox[0] == True:
                if prox[1] == 0: #VOLTAR
                    self.stat = "MENU"
        
        elif self.stat == "CREDITOS":
            prox = self.status[3].mouse()
            if prox[0] == True:
                if prox[1] == 0: #VOLTAR
                    self.stat = "MENU"

App(180, 80)