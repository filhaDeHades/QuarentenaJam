import pyxel
import coronajogador as cj
import obst as obs

class Jogo:
    player = cj.Coronajogador(0, 0)
    objetos = []
    for i in range(3):
        obst = obs.Obstaculos("PERDEU")
        objetos.append(obst)
    width = 0
    height = 0
    status = "PERDEU"
    def __init__(self, w, h):
        self.player.x = 20
        self.player.y = 25
        self.width = w
        self.height = h
        self.status = "JOGANDO"
        for i in self.objetos:
            i.setX(180)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit
        self.player.update()
        for i in self.objetos:
            i.update()
            i.setState("JOGANDO")

    def draw(self):
        pyxel.cls(3)
        pyxel.blt(0, 0, 1, 0, 0, 180, 80)
        self.player.draw()
        for i in self.objetos:
            i.draw()
    
    def mouse(self):
        if pyxel.btn(pyxel.KEY_ESCAPE):
            return [True, 0]
        return [False]