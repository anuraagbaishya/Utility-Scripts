from allClassesAndGlobalVariables import *
import pygame,math,random
slowFPS = 8 
cols = 320 
rows = 320 
pygame.init()
gameDisplay = pygame.display.set_mode((cols,rows))
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
def homeScreen(heart,stage,Shape,boObj):
    gameDisplay.fill(white)
    img = pygame.image.load("home.jpg")
    gameDisplay.blit(img,(0,0))
    while not heart._quit:
        for events in pygame.event.get():
                        if events.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        if events.type == pygame.KEYDOWN:
                                if events.key == pygame.K_c:
                                        playGame(heart,Shape,boObj,stage)
                                elif events.key == pygame.K_q:
                                    pygame.quit()
                                    quit()
        heart.out_message_centered("Welcome To AweTetriSome",blue,-rows/3)
        heart.out_message_centered("+10 score for each block added ",green,-rows/3+20)
        heart.out_message_centered("+100 score for each row completely full",green,-rows/3+40)
        heart.out_message_centered("Press 'c' to play .. ",green,rows-20)
        heart.out_message_centered("Press 'q' to quit .. ",green,rows-40)
        heart.out_message_centered("Press 'm' to goto main screen .. ",green,-rows/5 + 20) 
        pygame.display.update()
def gameOverScreen(heart,Shape,boObj):
    while 1:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_i:
                        instruction(quit,heart,boObj)
                elif events.key == pygame.K_r:
                        newBoardObject = Board(rows,cols);
                        newHeart = Gameplay(320,300,"GameOn");              
                        playGame(newHeart,Shape,newBoardObject,0)
                elif events.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif events.key == pygame.K_m:
                    boardObject = Board(rows,cols)
                    heart = Gameplay(320,300,"GameOn")
                    homeScreen(heart,0,shape,boardObject)
        gameDisplay.fill(white)
        heart.out_message_centered("GAME OVER",blue,-rows/3)
        heart.out_message_centered("Final Score = "+str(heart._score),green,-rows/12)
        heart.out_message_centered("Press 'r' to restart .. ",green,rows/10)
        heart.out_message_centered("Press 'q' to quit .. ",green,rows/4 - rows/60)
        heart.out_message_centered("Press 'm' to goto main screen .. ",green,rows/4 - rows/60 + 35) 
        pygame.display.update()
def playGame(heart,Shape,boardObject,stage):
    game = True
    score = 0
    rowsFullIndex = []
    rando = random.randint(0,until)
    while game == True:
        img = pygame.image.load(level[stage]._img)
        gameDisplay.blit(img,(10,10))
        board = boardObject._matrix
        X = cols/20
        Y = 0
        flag = 0
        sh = shape[rando].shapearr
        FPS = level[stage]._fps
        rotatedShape = sh
        prevShape = sh
        X_change=0
        while 1:
            boardObject.printScreen(stage,level[stage],shape[rando].IMAGE)
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
                        #print "yo"
                        occupied = 1
                        prevShape = rotatedShape;
                        rotatedShape = shape[rando].clockwise(rotatedShape)
                        out = boardObject.checkOutOfBounds(rotatedShape,X,Y)
                        if not out: occupied = boardObject.check_pos(rotatedShape,X,Y)
                        if occupied or out: rotatedShape = prevShape
                    elif event.key == pygame.K_RIGHT and X < (cols/10-len(rotatedShape[0])) and not flag:
                        if not boardObject.check_pos(rotatedShape,X+X_change+1,Y): X_change += 1 
                    elif event.key == pygame.K_LEFT and X > 0 and not flag:
                        if not boardObject.check_pos(rotatedShape,X+X_change-1,Y): X_change -= 1 
                    elif event.key == pygame.K_DOWN:
                        flag = 1
                        FPS = 5000
                elif event.type == pygame.KEYUP:
                    X_change = 0
            if not boardObject.check_pos(rotatedShape,X+X_change,Y):
                X=shape[rando].move(X,X_change)
            Y += 1
            ret = boardObject.check_pos(rotatedShape,X,Y)
            Y = Y - ret
            if Y < 0 : 
                gameOverScreen(heart,shape,boardObject)
            if X<0 : X=0
            if X >= cols/10 - len(rotatedShape[0]) : X = cols/10 - len(rotatedShape[0])
            shape[rando].printShape(rotatedShape,X,Y)
            rowsFullIndex = heart.checkRowFull(boardObject)
            numberOfFull = len(rowsFullIndex)
            #print numberOfFull
            score = heart.updateScore(0,numberOfFull)
#            print numberOfFull
            board = boardObject.bringDown(rowsFullIndex,boardObject._matrix)
            boardObject._matrix = board
            if not flag:
                FPS = level[stage]._fps
            if ret or Y >= rows/10 - len(rotatedShape):
                xx = random.randint(0,30)
                yy = random.randint(0,30)
                if boardObject._matrix[xx][yy] !=1 and stage>=2:
                    boardObject._matrix[xx][yy] = 2;
                    board[xx][yy] = 2
                FPS = level[stage]._fps
                flag = 0
                #print "Len",numberOfFull
                boardObject.fill(rotatedShape,X,Y)
                X = cols/20
                Y = 0
                pygame.display.update()
                rando = random.randint(0,until)
                rotatedShape = shape[rando].shapearr
                #print "just before score",numberOfFull
                score = heart.updateScore(1,0)
                boardObject.printScreen(stage,level[stage],shape[rando].IMAGE)
            heart.printScore()
            if score >= level[stage]._minScore: stage+=1
            for i in range(len(boardObject._matrix)):
                for j in range(len(boardObject._matrix)):
                    if board[i][j] == 2:
                        #print "lol"
                        img = pygame.image.load("golden.png");
                        gameDisplay.blit(img,(i*10,j*10))
            pygame.display.update()
            clock.tick(FPS)
shape = [ 
        allShapes([[1],[1],[1],[1]],"block.png",1,4),
        allShapes([[1,1]],"block.png",2,1),
        allShapes([[0,1,0],[1,1,1]],"block.png",3,2),
        allShapes([[1,1,0,0],[0,0,1,1]],"block.png",4,2),
        allShapes([[1,1],[1,1]],"block.png",2,2),
        allShapes([[1,1],[1,0]],"block.png",2,2),
        allShapes([[1,0,0],[1,1,1]],"block.png",3,2),
        allShapes([[1,0],[1,0],[1,0],[1,1]],"block.png",2,4),
        allShapes([[0,1,0],[1,1,1],[0,1,0]],"block.png",3,2),
        allShapes([[1,1,0],[0,1,1]],"block.png",4,2)
        ]
level = [ 
        Level(1,"level1.png",8,300),
        Level(2,"level2.png",12,600),
        Level(3,"level3.png",20,1000),
        Level(4,"level4.png",30,35000000)
        ]
boardObject = Board(rows,cols)
heart = Gameplay(320,300,"GameOn")
homeScreen(heart,0,shape,boardObject)
