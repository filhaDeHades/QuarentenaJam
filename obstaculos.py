import pyxel
from enum import Enum, unique, auto

obst_num= 15
obst_dis= 60
obst_speed= 1.8

way = [8,32,56,80,104]

@unique
class GameState(Enum):
    INIT = auto()
    START = auto()

class obstaculos:
    def __init__ (self):
        self.state = GameState.INIT
        self.obst_x = [10]*obst_num
        self.obst_y = [11]*obst_num
        self.obst_act=[False]*obst_num

        self.obst2_x = [10]*obst_num
        self.obst2_y = [11]*obst_num
        self.obst2_act=[False]*obst_num

        pyxel.load("assets/menu.pyxres")
        pyxel.run(self.update, self.draw)
       

    def update(self):
        if pyxel.btnp(pyxel.KEY_L):
            pyxel.quit()
        if self.state == GameState.START:
            self.update_obst()

        
        if pyxel.btnp(pyxel.KEY_SPACE) and (self.state != GameState.START):
            self.state = GameState.START
            self.obst_x = [10]*obst_num
            self.obst_y = [11]*obst_num
            self.obst_act=[False]*obst_num

            self.obst2_x = [10]*obst_num
            self.obst2_y = [11]*obst_num
            self.obst2_act=[False]*obst_num

    def update_obst(self):
        for i in range(5):
    #first obstáculo
            if self.obst_x[i] > 180:
                self.obst_act[i] = False
            if  self.obst_y ==  way[i] and self.obst_act[i] == False and self.obst_act[i+10] == True and self.obst_x[i+10] >= obst_dis:
                self.obst_reset(i,i)
            elif self.obst_y ==  way[i] and self.obst_act[i] == False and self.obst_act[i+10] == False:
                self.obst_reset(i,i)
            if self.obst_act[i] == True:
                self.obst_x[i] += obst_speed
    #second obstáculo            
            if  self.obst_act[i+5] == False and self.obst_act[i] == True and self.obst_x[i] >= obst_dis :
                self.obst_reset(i+5,i)
            if self.obst_act[i+5] == True:
                self.obst_x[i+5] += obst_speed
            if self.obst_x[i+5] > 180:
                self.obst_act[i+5] = False
                
    #third obstáculo
            if self.obst_act[i+10] == False and self.obst_act[i+5] == True and self.obst_x[i+5] >= obst_dis :
                self.obst_reset(i+10,i)
            if self.obst_act[i+10] == True:
                self.obst_x[i+10] += obst_speed
            if self.obst_x[i+10] > 180:
                self.obst_act[i+10] = False
            
            
    def obst_reset(self,i,way_num):
        pyxel.play(0,0,loop=False)
        if way_num >= 5:
            way_num = way_num - 5 
        self.obst_x[i] = 10     
        self.obst_y[i] = way[way_num]+3
        self.obst_act[i]=True

#####################################################################################
    def update_obst2(self):
        for i in range(5):
    #first obstáculo2
            if self.obst2_x[i] > 180:
                self.obst2_act[i] = False
            if  self.obst2_y ==  way[i] and self.obst2_act[i] == False and self.obst2_act[i+10] == True and self.obst2_x[i+10] >= obst_dis:
                self.obst2_reset(i,i)
            elif self.obst2_y ==  way[i] and self.obst2_act[i] == False and self.obst2_act[i+10] == False:
                self.obst2_reset(i,i)
            if self.obst2_act[i] == True:
                self.obst2_x[i] += obst_speed
    #second obstáculo2            
            if  self.obst2_act[i+5] == False and self.obst2_act[i] == True and self.obst2_x[i] >= obst_dis :
                self.obst2_reset(i+5,i)
            if self.obst2_act[i+5] == True:
                self.obst_x[i+5] += obst_speed
            if self.obst2_x[i+5] > 180:
                self.obst2_act[i+5] = False
                
    #third obstáculo2
            if self.obst2_act[i+10] == False and self.obst2_act[i+5] == True and self.obst2_x[i+5] >= obst_dis :
                self.obst2_reset(i+10,i)
            if self.obst2_act[i+10] == True:
                self.obst2_x[i+10] += obst_speed
            if self.obst2_x[i+10] > 180:
                self.obst2_act[i+10] = False
            
            
    def obst2_reset(self,i,way_num):
        pyxel.play(0,0,loop=False)
        if way_num >= 5:
            way_num = way_num - 5 
        self.obst2_x[i] = 10     
        self.obst2_y[i] = way[way_num]+25
        self.obst2_act[i]=True

    def draw(self):
        pyxel.cls(3)
        pyxel.blt(0, 0, 0, 0, 0, 180, 80)
        
        for i in range(obst_num):
            if self.obst_act[i] == True:
             pyxel.blt(self.obst_x[i], self.obst_y[i], 2, 16, 0, 23, 5,6) 

obstaculos()