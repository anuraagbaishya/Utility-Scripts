import pygame,random,math
import time
import sys
FPS = 10
gameDisplay = pygame.display.set_mode((300,320))
pygame.init()
cols = 300;
rows = 320;
red = (255,0,0)
black = (255,255,255)
white = (0,0,0)
rando = random.randint(0,2)
clock = pygame.time.Clock()
game= True
board=[];
def newBoard():
    #board = [ [ 0 for x in xrange(0,cols+10,10) ]
#                        for y in xrange(0,rows+10,10) ]
    #board += [[ 1 for x in xrange(0,cols+10,10)]]
    for i in range(0,rows/10+5):
        new = []
        for j in range(0,cols/10+5):
            new.append(0)
        board.append(new)
    print board
class Block:
    y=0
    #  def rotate():
    def move(self,change):
     #   self.unfillBoard();
        #self.x -= 1
        return X+change
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
        self.width = len(arr[0]);
        self.height = len(arr);
    def printShape(self,arr,X,Y):
        for i in range(self.height):
            for j in range(self.width):
                if arr[i][j] == 1:
                    img = pygame.image.load("block.png")
                    gameDisplay.blit(img,((X + j)*10,(Y + i)*10));
#                    print("yes")
        #py.display.update()
    def clockwise(self,New_shape):
            Shape = reversed(New_shape)
            Tr_shape = list(zip(*(Shape)))
            for Xvar in range(len(Tr_shape)):
                    Tr_shape[Xvar] = list(Tr_shape[Xvar])
            #print "clockwise"
            self.shapearr = Tr_shape
            return Tr_shape


shape = [
        allShapes([[1,1]],"3.jpeg",2,1),
        allShapes([[0,1,0],[1,1,1]],"3.jpeg",3,2),
        allShapes([[1,1,0,0],[0,0,1,1]],"3.jpeg",4,2),
        allShapes([[1],[1],[1],[1]],"3.jpeg",1,4),
        allShapes([[1,1],[1,1]],"3.jpeg",2,2),
        allShapes([[1,0,0],[1,1,1]],"3.jpeg",3,2),
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
    for i in xrange(0,cols/10 +2):
        for j in xrange(0,rows/10 + 2):
            #print i,j
              if board[i][j] == 1:
                gameDisplay.blit(img,((i)*10,(j)*10));
def fill(self,shape,X,Y):
    for i in xrange(0,self.height):
        for j in xrange(0,self.width):
            #print i,j
            if shape.shapearr[i][j] == 1:
                board[j+X][i+Y]=1;
           #     print X+j,Y+i

def check_pos(shape,X,Y):
    for Xvar in range(len(shape)):
        for Yvar in range(len(shape[0])):
            if shape[Xvar][Yvar] == 1:
                #print Yvar + X,Xvar + Y
                if (X + Yvar)*10 <= rows+10 and (Y + Xvar)*10 <=cols+10:
                    if board[Yvar + X][Xvar + Y] == 1:
                        return list(zip(*shape[Xvar:]))[Yvar].count(1)
    return 0
                
while game == True:
    newBoard()
    gameDisplay.fill(black)
    X = 15
    Y = 0
  #  sh = shape[rando]
   # rotatedShape = sh
    flag = 0
    X_change=0
    while 1:
        sh = shape[rando].shapearr
        rotatedShape = sh
        printScreen()
        #gameDisplay.fill(black)
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
                elif event.key == pygame.K_s:
                    print "yo"
                    prevShape = rotatedShape;
                    rotatedShape = shape[rando].clockwise(rotatedShape)
                    occupied = check_pos(rotatedShape,X,Y)
                    if occupied: rotatedShape = prevShape
                    else : 
                        temp = shape[rando].height
                        shape[rando].height = shape[rando].width
                        shape[rando].width = temp

                    
                elif event.key == pygame.K_RIGHT and X < (cols/10-shape[rando].width) and not flag:
                        if not check_pos(sh,X+X_change+1,Y): X_change += 1 
                elif event.key == pygame.K_LEFT and X > 0 and not flag:
                        if not check_pos(sh,X+X_change-1,Y): X_change -= 1 
                elif event.key == pygame.K_DOWN:
            #        prev = shape[rando].
                    flag = 1
                    FPS = 5000
            elif event.type == pygame.KEYUP:
                X_change = 0
        if not check_pos(sh,X+X_change,Y):
            X=shape[rando].move(X_change)
        Y += 1
        ret = check_pos(sh,X,Y)
        Y = Y - ret
      #  print 'Yes',ret
        if X<0 : X=0
        if X >= cols/10 - shape[rando].width : X = cols/10 - shape[rando].width
        shape[rando].printShape(rotatedShape,X,Y)
        #print board
        pygame.display.update()
#        print X,Y
        if not flag:
            FPS = 8
        if ret or Y >= 32 - shape[rando].height:
            FPS = 8
            flag = 0
            fill(shape[rando],X,Y)
            X = 15
            Y = 0
            pygame.display.update()
            rando = random.randint(0,2)
            printScreen()
        clock.tick(FPS)
