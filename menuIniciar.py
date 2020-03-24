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
        pyxel.blt(self.width/2-16, self.height/2, 0, 0, 0, 32, 29, 0)
    
    def mouse(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if pyxel.mouse_x >= self.width/2-16 and pyxel.mouse_x <= self.width/2-8:
                if pyxel.mouse_y >= self.height/2+8 and pyxel.mouse_y <= (self.height/2)+12: #MÚSICA ON
                    print([True, 0])
                    return [True, 0]
                    
            if pyxel.mouse_x >= self.width/2+1 and pyxel.mouse_x <= self.width/2+11: #MÚSICA OFF
                if pyxel.mouse_y >= self.height/2+8 and pyxel.mouse_y <= (self.height/2)+12:
                    print([True, 1])
                    return [True, 1]
            if pyxel.mouse_x >= self.width/2-16 and pyxel.mouse_x <= (self.width/2-16)+29: #Creditos
                if pyxel.mouse_y >= self.height/2+25 and pyxel.mouse_y <= self.height/2+29:
                    print([True, 2])
                    return [True, 2]
        
        return [False]