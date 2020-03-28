import pyxel
gravit = 0.8

class Coronajogador:
    x = 0
    y = 0
    vivo = True
    anim = [[0,96], [16,96]]
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self, tipo):
        pyxel.blt(self.x, self.y, 0, self.anim[tipo][0], self.anim[tipo][1], 16, 16, 3)

    def update(self):
        if self.y >= 65:
            self.estado(False)
        else:
            self.estado(True)
        if pyxel.btnr(pyxel.KEY_SPACE) or pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
            self.y = max(self.y -4 , 0)
            self.y = max(self.y -4 , 0)
            return 1
        else:
            self.y = min(self.y +gravit, 65)
            return 0
        
        
    def estado(self,jorge): 
        self.vivo = jorge