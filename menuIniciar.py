import pyxel

class Iniciar:
    width = 0
    height = 0
    def __init__(self, w, h):
        self.width = w
        self.height = h
       # self.play_music(True) 

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
           # self.play_music(True)

    def draw(self):
        pyxel.cls(3)
        pyxel.blt(self.width/2-40, 0, 0, 40, 32, 80, 48, 0)
        pyxel.text(73, 50, "INICIAR", pyxel.frame_count % 16)
        pyxel.blt(self.width/2-18, self.height/4*3, 0, 0, 0, 29, 18, 0)
    
    def mouse(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if pyxel.mouse_x >= self.width/2-18 and pyxel.mouse_x <= self.width/2-10:
                if pyxel.mouse_y >= self.height/4*3+7 and pyxel.mouse_y <= self.height/4*3+12: #MÚSICA ON
                    return [True, 0]
                    
            if pyxel.mouse_x >= self.width/2 and pyxel.mouse_x <= self.width/2+11: #MÚSICA OFF
                if pyxel.mouse_y >= self.height/4*3+7 and pyxel.mouse_y <= self.height/4*3+12:
                    return [True, 1]
            if pyxel.mouse_x >= self.width/2-18 and pyxel.mouse_x <= (self.width/2-18)+29: #Creditos
                if pyxel.mouse_y >= self.height/4*3+14 and pyxel.mouse_y <= self.height/4*3+18:
                    return [True, 2]
            if pyxel.mouse_x >= 73 and pyxel.mouse_x <= 101: #Iniciar
                if pyxel.mouse_y >= 50 and pyxel.mouse_y <= 55:
                    return [True, 3]
        
        return [False]