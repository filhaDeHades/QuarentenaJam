import pyxel

class Pause:
    width = 0
    height = 0
    def __init__(self, w, h):
        self.width = w
        self.height = h
        #pyxel.init(180, 80, caption="PAUSADO")
        #pyxel.load("assets/menu.pyxres")
        #self.play_music (True)
       # pyxel.run(self.update, self.draw)

    def play_music(self, ch0):
        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)

    def update(self):
        pyxel.mouse(True)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #if pyxel.btnp(pyxel.KEY_1):
            #self.play_music (True)

    def draw(self):
        pyxel.cls(3)
        pyxel.text(75, 10, "PAUSADO", pyxel.frame_count % 16)
        pyxel.blt(self.width/2-16, self.height/2, 0, 0, 0, 28, 16, 0)
        pyxel.blt(self.width/2-18, self.height/4*3, 0, 40, 0, 32, 16, 0)
        
#Pause(180, 80)