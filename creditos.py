import pyxel

class Creditos:
    var = 0
    seta = [[0, 8], [8, 8]]
    animSeta = 0
    height = 0
    width = 0

    credito = ['Desenvolvedores:', 'Amanda Melo', 'Eduardo Motta', 'Gabriel Vieira', 'Pedro Lanzarini', 'Tamires da Hora','', 'Musica:', 'Amanda Melo', 'Gabriel Vieira', '', 'Arte:', 'Gabriel Vieira', 'Pedro Lanzarini']
    credAlt = []

    def __init__(self, w, h):
        self.var = h
        self.height = h
        self.width = w
        
        self.preencherAlturas()
        #pyxel.init(self.width, self.height, caption="Créditos")
        
        #pyxel.run(self.update, self.draw)

    def update(self):
        pyxel.mouse(True)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        for i in range(len(self.credito)):
            self.credAlt[i] -= .5
        
        for j in range(len(self.credAlt)):
            if self.credAlt[j] < 20:
                self.credAlt[j] += 210
        
        if pyxel.mouse_x > 3 and pyxel.mouse_x < 11:
            if pyxel.mouse_y > self.height/16 and pyxel.mouse_y < self.height/16+8:
                self.animSeta = 1
            else:
                self.animSeta = 0
        else:
            self.animSeta = 0

    def draw(self):
        pyxel.cls(3)
        pyxel.blt(3, self.height/16, 0, self.seta[self.animSeta][0], self.seta[self.animSeta][1], 8, 8, 0)
        pyxel.blt(self.width/2-16, self.height/16, 0, 0, 0, 32, 8, 0)
        for i, j, k in zip(self.credito, self.credAlt, range(len(self.credito))):
            pyxel.text(self.width/3, j, i, 10)
    
    def preencherAlturas(self):
        maior = 1
        for i in range(len(self.credito)):
            c = self.var+10*i
            self.credAlt.append(c)
            if maior < c:
                maior = c
