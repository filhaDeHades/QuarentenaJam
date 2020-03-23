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
        if pyxel.btn(pyxel.KEY_SPACE):
            self.y = self.y -16 
            max.y = 80

        else:
            self.y = self.y +gravit
            min.y = 0

