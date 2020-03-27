import pyxel

class Iniciar:
    width = 0
    height = 0
    def __init__(self, w, h):
        self.width = w
        self.height = h
<<<<<<< HEAD
       # self.play_music(True) 
=======
        #self.play_music(True)
>>>>>>> 505d3b9e215fd4483b6dc36eb0a7e16c471788a0

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
<<<<<<< HEAD
           # self.play_music(True)
=======
        #   self.play_music(True)
>>>>>>> 505d3b9e215fd4483b6dc36eb0a7e16c471788a0

    def draw(self):
        pyxel.cls(3)
        pyxel.text(75, 30, "INICIAR", pyxel.frame_count % 16)
        pyxel.blt(self.width/2-16, self.height/2, 0, 0, 0, 32, 29, 0)
    
    def mouse(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if pyxel.mouse_x >= self.width/2-16 and pyxel.mouse_x <= self.width/2-8:
                if pyxel.mouse_y >= self.height/2+8 and pyxel.mouse_y <= (self.height/2)+12: #MÚSICA ON
                    return [True, 0]
                    
            if pyxel.mouse_x >= self.width/2+1 and pyxel.mouse_x <= self.width/2+11: #MÚSICA OFF
                if pyxel.mouse_y >= self.height/2+8 and pyxel.mouse_y <= (self.height/2)+12:
                    return [True, 1]
            if pyxel.mouse_x >= self.width/2-16 and pyxel.mouse_x <= (self.width/2-16)+29: #Creditos
                if pyxel.mouse_y >= self.height/2+25 and pyxel.mouse_y <= self.height/2+29:
                    return [True, 2]
            if pyxel.mouse_x >= 75 and pyxel.mouse_x <= 103: #Iniciar
                if pyxel.mouse_y >= 30 and pyxel.mouse_y <= 35:
                    print([True, 3])
                    return [True, 3]
        
        return [False]