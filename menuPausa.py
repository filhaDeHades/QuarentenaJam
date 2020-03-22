import pyxel

pause = ['']
width = 180
height = 80

class Pause:
    def __init__(self):
        pyxel.init(180, 80, caption="PAUSADO")
        pyxel.load("assets/restodopause.pyxres")
        pyxel.run(self.update, self.draw)
    

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(75, 10, "PAUSADO", pyxel.frame_count % 16)
        pyxel.blt(width/2-16, height/2, 0, 0, 0, 32, 50, 0)

Pause()