import pyxel

width = 180
height = 80
var = height
credito = ['Desenvolvedores:', 'Amanda Melo', 'Eduardo Motta', 'Gabriel Vieira', 'Pedro Lanzarini', 'Rafaela', 'Tamires da Hora', 'Musica:', 'Amanda Melo', 'Gabriel Vieira', 'Arte:', 'Gabriel Vieira', 'Pedro Lanzarini']
credAlt = [var, var+18, var+18*2, var+18*3, var+18*4, var+18*5, var+18*6, var+18*7, var+18*8, var+18*9, var+18*10, var+18*11, var+18*12]

class Creditos:
    def __init__(self):
        pyxel.init(width, height, caption="Créditos")
        pyxel.load("assets/creditos.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        for i in range(7):
            credAlt[i] -= .5

    def draw(self):
        pyxel.cls(3)
        pyxel.blt(width/2-16, height/16, 0, 0, 0, 32, 8, 0)
        for i in range(8):
            pyxel.text(width/3, credAlt[i], credito[i], 10)



Creditos()
