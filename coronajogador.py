import pyxel
gravit = 2

class Coronajogador:
    x = 0
    y = 0
    anim = [0,0]
    def __init__(self):
        pyxel.load("assets/corona.pyxres")
    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.anim[0], self.anim[1], 15, 15, 0)
    def update(self):
        pyxel.btn(pyxel.KEY_SPACE)

