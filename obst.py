import pyxel
from random import randint

class Obstaculos:
    obsX = 0
    obsY = 0
    obsSpeed = -2
    objeto = 0
    tipo = [[0,112],[16, 112],[32, 112],[48, 112], [64, 112], [80, 112], [96, 112], [112,112]]
    state = "PERDEU"
    def __init__(self, estado, y, img):
        self.obsY = y
        self.state = estado
        self.objeto = img
    
    def update(self):
        if self.state == "JOGANDO":
            self.setX(self.obsX + self.obsSpeed)

    def draw(self):
        pyxel.blt(self.obsX, self.obsY, 0, self.tipo[self.objeto][0], self.tipo[self.objeto][1], 16, 16, 12)

    def setPosition(self, x, y):
        self.obsX = x
        self.obsY = y
    
    def setX(self, x):
        self.obsX = x
    
    def setState(self, estado):
        self.state = estado