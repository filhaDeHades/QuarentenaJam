import pyxel

credito = ['']
width = 160
height = 112

class desenho:
    def __init__(self):
        pyxel.init(width, height, caption="Desenho")
        pyxel.load("assets/teste.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(width/2-80, height/112, 0, 0, 0, 160, 112, 0)



desenho()