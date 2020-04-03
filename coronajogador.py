import pyxel
gravit = 0.8

class Coronajogador:
    x = 0
    y = 0
    vivo = True
    anim = [[0,96], [16,96]]
    up = False
    count = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self, tipo):
        if self.up == True:
            pyxel.blt(self.x, self.y, 0, self.anim[1][0], self.anim[1][1], 16, 16, 3)
        else:
            pyxel.blt(self.x, self.y, 0, self.anim[0][0], self.anim[0][1], 16, 16, 3)

    def update(self):
        if self.y >= 65:
            self.estado(False)
        else:
            self.estado(True)
        if self.count == 5:
            self.count = 0
            self.up = False
        if pyxel.btnr(pyxel.KEY_SPACE) or pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
            self.up = True
            #return 1
        #else:
            #self.y = min(self.y +gravit, 65)
            #return 0
        if self.up == True:
            self.y = max(self.y - gravit*2, 0)
            self.count += 1
        else:
            self.y = min(self.y +gravit, 65)
        
    def estado(self,jorge): 
        self.vivo = jorge