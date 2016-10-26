import pygame,random
import time
import sys
FPS = 5
gameDisplay = pygame.display.set_mode((300,320))
pygame.init()
cols = 300;
rows = 320;
red = (255,0,0)
black = (255,255,255)
white = (0,0,0)
rando = random.randint(0,7)
clock = pygame.time.Clock()
game= True
board=[];
def newBoard():
    #board = [ [ 0 for x in xrange(0,cols+10,10) ]
#                        for y in xrange(0,rows+10,10) ]
    #board += [[ 1 for x in xrange(0,cols+10,10)]]
    for i in range(0,rows+102,10):
        new = []
        for j in range(0,cols+102,10):
            new.append(0)
        board.append(new)
#    board += [[ 1 for x in xrange(0,cols+1,10)]]
    print board
class Block:
    y=0
    #  def rotate():
    def moveLeft(self):
     #   self.unfillBoard();
        self.x -= 1
      #  self.fillBoard();
    def moveRight(self):
   #     self.unfillBoard();
        self.x += 1
    #    self.fillBoard();
    def moveDown(self):
 #       self.unfillBoard();
        self.y = 32 - (self.height)
  #      self.fillBoard();
#    def unfillBoard(self):
      #  print("unfill")
       # for i in range(self.height):
        #    for j in range(self.width):
         #       board[self.x + i][self.y + j] = 0
def fillBoard(X,Y,height,width):
    for i in range(height):
        for j in range(width):
            board[X + i][Y + j]=1

        


class allShapes(Block):
    def __init__(self,arr,img,width,height):
        self.x = cols/20;
        self.image = img;
        self.y = 0;
        self.shapearr = arr;
        self.width = width;
        self.height = height;
    def printShape(self,X,Y):
        for i in range(self.height):
            for j in range(self.width):
                if self.shapearr[i][j] == 1:
                    img = pygame.image.load("block.png")
                    gameDisplay.blit(img,((X + j)*10,(Y + i)*10));
#                    print("yes")
        #pygame.display.update()

shape = [
        allShapes([[1,1,1,1]],"3.jpeg",4,1),
        allShapes([[1,1,0,0],[0,0,1,1]],"3.jpeg",4,2),
        allShapes([[1],[1],[1],[1]],"3.jpeg",1,4),
        allShapes([[1,1],[1,1]],"3.jpeg",2,2),
        allShapes([[1,1]],"3.jpeg",2,1),
        allShapes([[1,0,0],[1,1,1]],"3.jpeg",3,2),
        allShapes([[0,1,0],[1,1,1]],"3.jpeg",3,2),
        allShapes([[1,0],[1,0],[1,0],[1,1]],"3.jpeg",2,4)
        ]
class Gameplay:
    x=0;
#    def checkRowFull():
 #   def updateScore():
  
  #def selectPiece():
class Board(Gameplay):
    z=0;
   # def checkPiecePos():
    
    #def fillPiecePos():

    #def moveRight():
   # def draw():
def printScreen():
    gameDisplay.fill(black)
    img = pygame.image.load("block.png")
    for i in xrange(0,cols/10-1):
        for j in xrange(0,rows/10-1):
            #print i,j
              if board[i][j] == 1:
                gameDisplay.blit(img,((i+1)*10,(1+j)*10));
def fill(shape,X,Y):
    for i in xrange(0,shape.height):
        for j in xrange(0,shape.width):
            #print i,j
            if shape.shapearr[i][j] == 1:
                board[j+X-1][i+Y-1]=1;
                print X+j-1,Y+i-1

def check_pos(shape,X,Y):
    for Xvar in range(len(shape)):
        for Yvar in range(len(shape[0])):
            if shape[Xvar][Yvar] == 1:
                print Yvar + X,Xvar + Y
                if board[Yvar + X-1][Xvar + Y-1] == 1:
                    return 1
    return 0
                
while game == True:
    newBoard()
    gameDisplay.fill(black)
    while 1:
        sh=shape[rando]
        Y = sh.y
        X = sh.x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    game = False
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_RIGHT and sh.x < (cols/10-sh.width):
                    checkPos(sh)

            #        print sh.x,cols,sh.width
                    shape[rando].moveRight()
                elif event.key == pygame.K_LEFT and sh.x > 0:
                    shape[rando].moveLeft();
                elif event.key == pygame.K_DOWN:
            #        prev = sh.
                    shape[rando].moveDown()
        printScreen()
        #gameDisplay.fill(black)
        Y += 1
        ret = check_pos(sh.shapearr,X,Y)
        Y = Y - ret
        
        pygame.display.update()
        shape[rando].printShape(X,Y)
       # for i in xrange(0,shape.height):
        #    for j in xrange(0,shape.width):
         #       #print i,j
          #      if shape.shapearr[i][j] == 1:
           #         board[j+shape.x-1][i+shape.y-1]=1;
                   # print shape.x+j,shape.y+i
        if ret or Y >= 32 - sh.height:
            rando = random.randint(0,7)
            fill(sh,X,Y)
            #fill(sh)
            printScreen()
        clock.tick(FPS+10)
