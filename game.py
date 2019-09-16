import pyxel
import random
import pyxelChara as Chara

WIDTH = 128
HEIGHT = 128

class App:
    my_x = 0
    my_y = 0
    interval = 30
    cnt = 0
    enemyList = []

    def __init__(self):  
        pyxel.init(WIDTH, HEIGHT)
        pyxel.load('quest.pyxres')

        self.myChara = Chara.MyChara()
        pyxel.run(self.update, self.draw)

    def makeEnemy(self):
        self.enemyList.append(Chara.Enemy(WIDTH, HEIGHT))

    def checkTimer(self):
        bRet = False
        self.cnt = (self.cnt + 1) % self.interval
        if(self.cnt == 0):
            bRet = True
        return bRet

    def update(self):
        self.my_x = pyxel.mouse_x
        self.my_y = pyxel.mouse_y
        if(self.checkTimer() == True):
            self.makeEnemy()

        for i in reversed(range(0, len(self.enemyList))):
            if(self.isCollision(i, self.my_x, self.my_y) == True):
                
                self.myChara.startAnimation()
                self.enemyList[i].startAnimation()

            if(self.enemyList[i].delete_flg == True):
                del self.enemyList[i]
                

    def isCollision(self, _i, _x, _y):
        bRet = False
        my_x = _x + 8
        my_y = _y + 8
        if(self.enemyList[_i].ani_flg != True 
            and self.enemyList[_i].delete_flg == False):
            if(
                (self.enemyList[_i].x <= my_x)
                and (self.enemyList[_i].x + 16 >= my_x)
                and (self.enemyList[_i].y <= my_y)
                and (self.enemyList[_i].y + 16 >= my_y)
            ):
                bRet = True
        return bRet

    def drawMap(self):
        tm = 0
        w = int(WIDTH / 8)
        h = int(HEIGHT / 8)
        pyxel.bltm(0,0,tm,0, 0,w,h)

    def draw(self):
        pyxel.cls(7)
        self.drawMap()
        for i in reversed(range(0, len(self.enemyList))):
            x = self.enemyList[i].x
            y = self.enemyList[i].y
            if(self.enemyList[i].delete_flg == False):
                self.enemyList[i].drawImage(x, y)

        self.myChara.drawImage(self.my_x, self.my_y)
App()
