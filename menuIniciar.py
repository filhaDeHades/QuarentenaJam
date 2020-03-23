# -- coding: utf-8 --
import pyxel

width = 180
height = 80

class Menuiniciar:
    def __init__(self):
        #pyxel.init(width, height, caption="menu")
        pyxel.load("assets/menu.pyxres")
        #pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(3)
        pyxel.blt(width/2-16, height/16, 0, 20, 11, 48, 12, 8)
        pyxel.blt(width/2-16, height/16*4, 0, 20, 26, 47, 13, 8)
        pyxel.blt(width/2-16, height/16*8, 0, 20, 43, 48, 12, 8)

Menuiniciar()