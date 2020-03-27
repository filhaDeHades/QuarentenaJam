import pyxel
from random import randint

class Obstaculos:
    posY = [0, 16, 32, 48, 64] #Posições fixas do Y
    obsX = 0
    obsY = 0
    obsSpeed = -1
    objeto = randint(0,3)
    tipo = [[0,112],[16, 112],[32, 112],[48, 112]]
    state = "PERDEU"
    def __init__(self, estado):
        self.state = estado
    
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