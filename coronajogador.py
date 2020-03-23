import pyxel
gravit = 2

class Coronajogador:
    x = 0
    y = 0
    vivo = True
    anim = [0,0]
    def __init__(self):
        pyxel.load("assets/corona.pyxres")
    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.anim[0], self.anim[1], 15, 15, 0)
    def update(self):
        if pyxel.btn(pyxel.KEY_SPACE):
            self.y = max(self.y -16 , 0)
        else:
            self.y = min(self.y +gravit, 80)
        
        if self.y >= 80:
            self.estado(False)
        else:
            self.estado(True)
    def estado(self,jorge): 
        self.vivo = jorge

Coronajogador()