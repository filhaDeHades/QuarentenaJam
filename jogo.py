import pyxel
import coronajogador as cj

class Jogo:
    player = cj.Coronajogador(0, 0)
    width = 0
    height = 0
    def __init__(self, w, h):
        self.player.x = 20
        self.player.y = 25
        self.width = w
        self.height = h

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit
        self.player.update()

    def draw(self):
        pyxel.cls(3)
        pyxel.blt(0, 0, 1, 0, 0, 180, 80)
        self.player.draw()
    
    def mouse(self):
        if pyxel.btn(pyxel.KEY_ESCAPE):
            return [True, 0]
        return [False]