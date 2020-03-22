import pyxel

width = 180
height = 80
var = height
seta = [[0, 8], [8, 8]]
animSeta = 0

credito = ['Desenvolvedores:', 'Amanda Melo', 'Eduardo Motta', 'Gabriel Vieira', 'Pedro Lanzarini', 'Rafaela', 'Tamires da Hora','', 'Musica:', 'Amanda Melo', 'Gabriel Vieira', '', 'Arte:', 'Gabriel Vieira', 'Pedro Lanzarini']
credAlt = []

maior = 0
for i in range(len(credito)):
    c = var+10*i
    credAlt.append(c)
    if maior < c:
        maior = c

class Creditos:
    
    def __init__(self):
        
        pyxel.init(width, height, caption="Créditos")
        pyxel.load("assets/creditos.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        pyxel.mouse(True)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        for i in range(len(credito)):
            credAlt[i] -= .5
        
        for j in range(len(credAlt)):
            if credAlt[j] < 20:
                credAlt[j] += 210
        
        if pyxel.mouse_x > 3 and pyxel.mouse_x < 11:
            if pyxel.mouse_y > height/16 and pyxel.mouse_y < height/16+8:
                animSeta = 1
        else:
            animSeta = 0


    def draw(self):
        pyxel.cls(3)
        pyxel.blt(3, height/16, 0, seta[animSeta][0], seta[animSeta][1], 8, 8, 0)
        pyxel.blt(width/2-16, height/16, 0, 0, 0, 32, 8, 0)
        for i, j, k in zip(credito, credAlt, range(len(credito))):
            pyxel.text(width/3, j, i, 10)



Creditos()
