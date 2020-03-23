import pyxel

pause = ['']
width = 180
height = 80

class Pause:
    def __init__(self):
        pyxel.init(180, 80, caption="PAUSADO")
        pyxel.load("assets/pause.pyxres")
        self.play_music (True)
        pyxel.run(self.update, self.draw)

    def play_music(self, ch0):
        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)

    def update(self):
        pyxel.mouse(True)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_1):
            self.play_music (True)

    def draw(self):
        pyxel.cls(3)
        pyxel.text(75, 10, "PAUSADO", pyxel.frame_count % 16)
        pyxel.blt(width/2-16, height/2, 0, 0, 0, 32, 50, 0)
        
Pause()