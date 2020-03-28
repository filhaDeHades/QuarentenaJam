import pyxel
fundos = [[[0,88], 1],[[0,88],2],[[0,0],2],[[0,0],1]]
class Fundo:
    x = 0
    y = 0
    w = 0
    h = 0
    tipo = 0
    def __init__(self, x, y, w, h, t):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.tipo = t


    def update(self):
        self.x -= 1


    def draw(self):
        pyxel.blt(self.x, self.y, fundos[self.tipo][1], fundos[self.tipo][0][0], fundos[self.tipo][0][1], self.w, self.h)