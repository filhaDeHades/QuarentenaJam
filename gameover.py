import pyxel

class GameOver:
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

        #if pyxel.btnp(pyxel.KEY_1):
            #self.play_music (True)

    def draw(self):
        pyxel.cls(3)
        pyxel.text(75, 10, "GAME OVER", pyxel.frame_count % 16)
        pyxel.blt(self.width/2-16, self.height/2, 0, 0, 0, 28, 16, 0)
        pyxel.blt(self.width/2-18, self.height/4*3, 0, 40, 0, 32, 16, 0)
    
    def mouse(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if pyxel.mouse_x >= self.width/2-18+7 and pyxel.mouse_x <= (self.width/2-18)+7+18: #JOGAR
                if pyxel.mouse_y >= self.height/4*3 and pyxel.mouse_y <= (self.height/4*3)+4:
                    return [True, 2]
            if pyxel.mouse_x >= self.width/2-18+10 and pyxel.mouse_x <= self.width/2-18+21: #SAIR N FUNCIONA
                if pyxel.mouse_y >= (self.height/4*3)+9 and pyxel.mouse_y <= (self.height/4*3)+14:
                    return [True, 3]
        
        return [False]
                
        
#GameOver(180, 80)