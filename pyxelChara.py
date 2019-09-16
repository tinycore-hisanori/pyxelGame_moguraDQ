import pyxel
import random

IMG_NO = 0
ENEMY_IMG_NO = 1

class MyChara:
    ani_no = 0
    ani_max = 5
    ani_interval = 2
    ani_cnt = 0
    ani_flg = False

    def __init__(self):
        self.x = pyxel.mouse_x
        self.y = pyxel.mouse_y
        self.ani_flg = False

    def startAnimation(self):
        self.ani_cnt = -1
        self.ani_no = 0
        self.ani_flg = True

    def drawImage(self, _my_x, _my_y):
        if(self.ani_flg == True):
            self.ani_cnt = ( self.ani_cnt + 1 ) % self.ani_interval
            if(self.ani_cnt == 0):
                self.ani_no = self.ani_no + 1
                if(self.ani_no >= self.ani_max):
                    self.ani_no = 0
                    self.ani_flg = False
        else:
            self.ani_no = 0        
        pyxel.blt(
            _my_x, _my_y,
            IMG_NO,
            0 + (self.ani_no * 16), 0,
            16, 16, 1)

class Enemy:
    ani_no = 0
    ani_max = 5
    ani_interval = 2
    ani_cnt = 0
    ani_flg = False
    delete_flg = False
    enm_no = 0
    def __init__(self, _width, _height):
        self.x = random.randint(0, _width)
        self.y = random.randint(0, _height)
        self.delete_flg = False
        self.enm_no = random.randint(0, 3)
    def startAnimation(self):
        if(self.ani_flg == False):
            self.ani_cnt = -1
            self.ani_no = 0
            self.ani_flg = True

    def drawImage(self, _x, _y):
        if(self.ani_flg == True):
            self.ani_cnt = ( self.ani_cnt + 1 ) % self.ani_interval
            if(self.ani_cnt == 0):
                self.ani_no = self.ani_no + 1
                if(self.ani_no >= self.ani_max):
                    self.ani_no = self.ani_max - 1
                    self.ani_flg = False
                    self.delete_flg = True
        else:
            self.ani_no = 0        
        pyxel.blt(
            _x, _y, ENEMY_IMG_NO,
            0 + (self.ani_no * 16), 0 + (self.enm_no * 16),
            16, 16, 1)
