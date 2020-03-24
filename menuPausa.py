import pyxel

class Pause:
    width = 0
    height = 0
    def __init__(self, w, h):
        self.width = w
        self.height = h
        #self.play_music (True)

    def play_music(self, ch0):
        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)

    def update(self):
        pyxel.mouse(True)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.mouse()

        #if pyxel.btnp(pyxel.KEY_1):
            #self.play_music (True)

    def draw(self):
        pyxel.cls(3)
        pyxel.text(75, 10, "PAUSADO", pyxel.frame_count % 16)
        pyxel.blt(self.width/2-16, self.height/2, 0, 0, 0, 28, 16, 0)
        pyxel.blt(self.width/2-18, self.height/4*3, 0, 40, 0, 32, 16, 0)
    
    def mouse(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if pyxel.mouse_x >= self.width/2-16 and pyxel.mouse_x <= (self.width/2-16)+8:
                if pyxel.mouse_y >= self.height/2+8 and pyxel.mouse_y <= (self.height/2)+12: #MÚSICA ON
                    print([True, 0])
            elif pyxel.mouse_x >= self.width/2+1 and pyxel.mouse_x <= self.width/2+11: #MÚSICA OFF
                if pyxel.mouse_y >= self.height/2+8 and pyxel.mouse_y <= (self.height/2)+12:
                    print([True, 1])
            elif pyxel.mouse_x >= self.width/2-18+7 and pyxel.mouse_x <= (self.width/2-18)+7+18: #JOGAR
                if pyxel.mouse_y >= self.height/4*3 and pyxel.mouse_y <= (self.height/4*3)+4:
                    print([True, 2])
            elif pyxel.mouse_x >= self.width/2-18+10 and pyxel.mouse_x <= (self.width/2-18)+21: #SAIR N FUNCIONA
                if pyxel.mouse_y >= (self.height/4*3)+8 and pyxel.mouse_y <= (self.height/4*3)+13:
                    print([True, 3])
                
        
#Pause(180, 80)