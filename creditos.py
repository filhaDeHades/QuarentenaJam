import pyxel

credito = ['']
width = 180
height = 80

class Creditos:
    def __init__(self):
        pyxel.init(width, height, caption="Créditos")
        pyxel.load("assets/creditos.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(3)
        pyxel.blt(width/2-16, height/16, 0, 0, 0, 32, 8, 0)



Creditos()
