import pyxel
import menuIniciar as mi
#import menuPausa
#simport jogo
import creditos as c

class App:
    stat = "MENU"         #estados possiveis: "MENU"; "PAUSA"; "JOGO"; "CREDITOS";
    status = [mi.Iniciar(180, 80), c.Creditos(180, 80)]
    width = 0
    height = 0
    def __init__(self, w, h):
        self.width = w
        self.height = h
        pyxel.init(self.width, self.height)
        #pyxel.load("assets/music.pyxres")
        pyxel.load("assets/menu.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_1):
            self.stat = "PAUSA"
            
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

App(180, 80)