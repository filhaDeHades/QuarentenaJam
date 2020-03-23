import pyxel

class Iniciar:
    width = 0
    height = 0
    def __init__(self, w, h):
        self.width = w
        self.height = h
        #self.play_music(True)

    def play_music(self, ch0):
        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)

    def update(self):        
        pyxel.mouse(True)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #if pyxel.btn(pyxel.KEY_1):
            #self.play_music(True)

    def draw(self):
        pyxel.cls(3)
        pyxel.text(75, 30, "INICIAR", pyxel.frame_count % 16)
        pyxel.blt(self.width/2-16, self.height/2, 0, 0, 0, 32, 50, 0)