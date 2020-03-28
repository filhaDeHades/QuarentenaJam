import pyxel

class GameOver:
    width = 0
    height = 0
    pontos = 0
    def __init__(self, w, h):
        self.width = w
        self.height = h
        #self.play_music (True)

    def play_music(self, ch0):
        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)

    def update(self, p = 0):
        self.pontos = p
        pyxel.mouse(True)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #if pyxel.btnp(pyxel.KEY_1):
            #self.play_music (True)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(71, 10, "GAME OVER", pyxel.frame_count % 16)
        pyxel.text(85, 20, f"{self.pontos}", pyxel.frame_count % 16)
        pyxel.text(77, 30, "pontos", pyxel.frame_count % 16)
        pyxel.blt(self.width/2-16, self.height/2, 0, 0, 0, 29, 12, 0)
        pyxel.blt(self.width/2-18, self.height/4*3, 0, 40, 0, 32, 16, 0)
    
    def mouse(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if pyxel.mouse_x >= self.width/2-16 and pyxel.mouse_x <= (self.width/2-16)+8:
                if pyxel.mouse_y >= self.height/2+8 and pyxel.mouse_y <= (self.height/2)+12: #MÚSICA ON
                    return [True, 0]
            if pyxel.mouse_x >= self.width/2+1 and pyxel.mouse_x <= self.width/2+11: #MÚSICA OFF
                if pyxel.mouse_y >= self.height/2+8 and pyxel.mouse_y <= (self.height/2)+12:
                    return [True, 1]
            if pyxel.mouse_x >= self.width/2-18+10 and pyxel.mouse_x <= self.width/2-18+21: #SAIR
                if pyxel.mouse_y >= (self.height/4*3)+9 and pyxel.mouse_y <= (self.height/4*3)+14:
                    return [True, 2]
        
        return [False]
                
        
#GameOver(180, 80)