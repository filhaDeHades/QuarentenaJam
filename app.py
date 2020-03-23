import pyxel
#import menuIniciar
#import menuIniciar
#simport jogo
import creditos

class App:
    stat = "CREDITOS"         #estados possiveis: "MENU"; "PAUSA"; "JOGO"; "CREDITOS";
    status = [creditos.Creditos(180, 80)]
    width = 0
    height = 0
    def __init__(self, w, h):
        self.width = w
        self.height = h
        pyxel.init(self.width, self.height)
        pyxel.load("assets/creditos.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if self.stat == "CREDITOS":
        #    self.c.update()
            self.status[0].update()

    def draw(self):
        pyxel.cls(3)
        if self.stat == "CREDITOS":
            self.status[0].draw()

App(180, 80)