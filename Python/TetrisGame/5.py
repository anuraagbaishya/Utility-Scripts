import pygame,random,math
import time
import sys
slowFPS = 8
cols = 320
rows = 320
gameDisplay = pygame.display.set_mode((cols,rows))
pygame.init()
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
maroon = (128,0,0)
green = (0,128,0)
purple = (128,0,128)
bluish = (0,128,128)
navy = (0,0,128)
lime = (0,255,0)
magenta = (255,0,255)
grey = (128,128,128)
until = 9;
blockSize = 10
clock = pygame.time.Clock()
class Block:
    def move(self,X,change):
        return X+change
class allShapes(Block):
    def __init__(self,arr,img,width,height):
        self.x = cols/20;
        self.image = img;
        self.y = 0;
        self.shapearr = arr;
        self.width = len(arr[0]);
        self.height = len(arr);
    def printShape(self,shapeArr,X,Y):
        for i in range(len(shapeArr)):
            for j in range(len(shapeArr[0])):
                if shapeArr[i][j] == 1:
                    img = pygame.image.load("block.png")
                    gameDisplay.blit(img,((X + j)*10,(Y + i)*10));
#                    print("yes")
        #py.display.update()
    def clockwise(self,New_shape):
            Shape = reversed(New_shape)
            Tr_shape = list(zip(*(Shape)))
            for Xvar in range(len(Tr_shape)):
                    Tr_shape[Xvar] = list(Tr_shape[Xvar])
            print "clockwise"
            #self.shapearr = Tr_shape
            return Tr_shape

class Board:
    z=0;
    def __init__(self,rows,cols):
        self._xmax = rows;
        self._ymax = cols;
        self._matrix = self.newBoard(rows,cols)
    def newBoard(self,row,col):
        var=[];
        for i in range(0,row/10+1):
            new = []
            for j in range(0,col/10+1):
                new.append(0)
            var.append(new)
        return var
    def fillBoard(self,X,Y,height,width):
        for i in range(height):
            for j in range(width):
                self._matrix[X + i][Y + j]=1
    def check_pos(self,shapeArr,X,Y):
        for Xvar in range(len(shapeArr)):
            for Yvar in range(len(shapeArr[0])):
                if shapeArr[Xvar][Yvar] == 1:
                    #print Yvar + X,Xvar + Y
                    if (X + Yvar)*10 <= rows+10 and (Y + Xvar)*10 <=cols+10:
                        if self._matrix[Yvar + X][Xvar + Y] == 1:
                            return list(zip(*shapeArr[Xvar:]))[Yvar].count(1)
        return 0
    def checkOutOfBounds(self,shapeArr,X,Y):
        for Xvar in range(len(shapeArr)):
            for Yvar in range(len(shapeArr[0])):
                if shapeArr[Xvar][Yvar] == 1:
                    #print Yvar + X,Xvar + Y
                    if not( (X + Yvar)*10 <= rows and (Y + Xvar)*10 <=cols): 
                            return 1
        return 0

    def bringDown(self,Full,Enter):
                #print "bring down"
                Full_row = sorted(Full)

#               print Full_row
                c = Enter
#                print Enter[31]
                Enter_temp = list(zip(*Enter))
                for X_r in range(len(Enter_temp)):
                        Enter_temp[X_r] = list(Enter_temp[X_r])
                for F_r in Full_row:
#                       for X_r in range(F_r,-1,-1):
#                               if X_r == 0: Enter_temp[0] = [0]*len(Enter_temp[0])
#                               else : Enter_temp[X_r] = Enter_temp[X_r - 1]
                        #print 'Ghusa!'
                        del(Enter_temp[F_r])
                        Enter_temp = [[0]*rows] + Enter_temp
                #print Enter_temp[30]
                Enter_new = list(zip(*Enter_temp))
#               print len(c),len(Enter_new)
                for Yr in range(len(Enter_new)): Enter_new[Yr] = list(Enter_new[Yr])
               # print Enter_new
                return Enter_new
    def printScreen(self,stage):
        pygame.draw.rect(gameDisplay,white,[0,0,cols+120,rows],0)
        pygame.draw.rect(gameDisplay, bluish, [0,320,520,440],0)
        heart.out_message_centered("Score: ",purple,rows-60)
        #pygame.draw.line(gameDisplay,blue,[0,0],[0,cols],10)
        pygame.draw.polygon(gameDisplay, blue, [[0,0],[rows,0],[0,cols],[rows,cols]],10)
        #pygame.draw.polygon(gameDisplay, blue, [[0,0],[0,cols],[rows,0],[rows,cols]],10)
        img = pygame.image.load(level[stage]._img)
        level[stage].blitImage(0,0)
        img = pygame.image.load("block.png")
        for i in range(0,cols/10):
            for j in range(0,rows/10):
                #print i,j
                  if self._matrix[i][j] == 1:
                    gameDisplay.blit(img,((i)*10,(j)*10));
    def fill(self,shapeArr,X,Y):
        for i in xrange(0,len(shapeArr)):
            for j in xrange(0,len(shapeArr[0])):
                #print i,j
                if shapeArr[i][j] == 1:
                    self._matrix[j+X][i+Y]=1;
class Gameplay(Board):
    xExtra = 120;
    yExtra = 200
    def __init__(self,row,col,title):
        self._score = 0
        self._row = row
        self._col = col
        self._pcInc = 10
        self._rwInc = 100
        self._gameSurface = pygame.display.set_mode((row+self.xExtra,col+self.yExtra))
        self.setCaption(title)
        self._font = pygame.font.SysFont(None,25)
        pygame.display.update()
        self._quit = False
    def updateScore(self,ten,hundred):
        if hundred: self._score += 100*hundred
        elif ten: self._score += 10
        return self._score
    def printScore(self):
        self.out_message_centered(str(self._score),green,rows-20)
    def setCaption(self,title):
        pygame.display.set_caption(title)
    def checkRowFull(self,boardObj):
        fullr=[]
        var = 1;
        for index in range(len(boardObj._matrix[0])):
            for it in range(len(boardObj._matrix)-1):
                if var != boardObj._matrix[it][index]:
          #          print "no",index
                    break
                if it == len(boardObj._matrix)-2:
                    fullr.append(index);
         #           print "yes",index
        return (fullr)
    def out_message_centered(self,text,color,displace = 0):
        out_msg = self._font.render(text,True,color)
        display_at = out_msg.get_rect()
        display_at.center = ((self._row + self.xExtra)/2 , self._col/2 + displace)
        self._gameSurface.blit(out_msg,display_at)

class Level:
    def __init__(self,no,image,FPS,miniScore):
        self._lev = no
        self._img = image
        self._fps = FPS
        self._minScore = miniScore
    def blitImage(self,x,y):
        img = pygame.image.load(self._img)
        gameDisplay.blit(img,(x,y))

shape = [
        allShapes([[1],[1],[1],[1]],"3.jpeg",1,4),
        allShapes([[1,1]],"3.jpeg",2,1),
        allShapes([[0,1,0],[1,1,1]],"3.jpeg",3,2),
        allShapes([[1,1,0,0],[0,0,1,1]],"3.jpeg",4,2),
        allShapes([[1,1],[1,1]],"3.jpeg",2,2),
        allShapes([[1,1],[1,0]],"3.jpeg",2,2),
        allShapes([[1,0,0],[1,1,1]],"3.jpeg",3,2),
        allShapes([[1,0],[1,0],[1,0],[1,1]],"3.jpeg",2,4),
        allShapes([[0,1,0],[1,1,1],[0,1,0]],"3.jpeg",3,2),
        allShapes([[1,1,0],[0,1,1]],"3.jpeg",4,2)
        ]
level = [
        Level(1,"level1.png",8,100),
        Level(2,"level2.png",20,1000),
        Level(3,"level3.png",20,5000),
        Level(4,"level3.png",30,1000000)
        ]


