
#chess
import random
from cmu_graphics import *
'''
Chess game

todo:
- caste
- AI choose a random piece make a valid move
- maye make a list of lost pieces
- record all moves and make undo
'''

app.board = []

def drawBoard():
    for x in range(0,401,50):
        Line(x,0,x,400,lineWidth=1)
    for y in range(0,401,50):
        Line(0,y,400,y,lineWidth=1)
    for x in range(0,401,50):
        for y in range(0,401,50):
            if (x/50)%2==1 and (y/50)%2==0:
                Rect(x,y,50,50,fill='grey')
            if (x/50)%2==0 and (y/50)%2==1:
                Rect(x,y,50,50,fill='grey')

def setBoard():
    for _ in range(8):
        app.board.append([0,0,0,0,0,0,0,0])
    app.board[0] = []
    app.board[1] = []
    app.board[6] = []
    app.board[7] = []
    app.board[0].append(Rook('black',0, 0))
    app.board[0].append(Knight('black',50, 0))
    app.board[0].append(Bishop('black',100,0))
    app.board[0].append(Queen('black',150,0))
    app.board[0].append(King('black',200,0))
    app.board[0].append(Bishop('black',250,0))
    app.board[0].append(Knight('black',300, 0))
    app.board[0].append(Rook('black',350, 0))

    for x in range(0,400,50):
        #Label('P', x-25, 25, size=24)
        app.board[1].append(Pawn('black',x, 50))
    
    for x in range(0,400,50):
        #Label('P', x-25, 25, size=24)
        app.board[6].append(Pawn('purple',x, 300))
    app.board[7].append(Rook('purple',0, 350))
    app.board[7].append(Knight('purple',50, 350))
    app.board[7].append(Bishop('purple',100,350))
    app.board[7].append(Queen('purple',150,350))
    app.board[7].append(King('purple',200,350))
    app.board[7].append(Bishop('purple',250,350))
    app.board[7].append(Knight('purple',300, 350))
    app.board[7].append(Rook('purple',350, 350))

        
class Pawn():
    def __init__(self,color,x,y):
        self.color=color
        self.label = Group( 
                        Rect(x+10, y+10,30, 30,fill='lightgrey'),
                        Label('P', x+25, y+25, size=24, fill=color),

                    )
        

class Rook():
    def __init__(self,color,x,y):
        self.color=color
        self.label = Group( 
                        Rect(x+10, y+10,30, 30,fill='lightgrey'),
                        Label('R', x+25, y+25, size=24, fill=color),

                    )
        

class Bishop():
    def __init__(self,color,x,y):
        self.color=color
        self.label = Group( 
                        Rect(x+10, y+10,30, 30,fill='lightgrey'),
                        Label('B', x+25, y+25, size=24, fill=color),

                    )
        
        
class Knight():
    def __init__(self,color,x,y):
        self.color=color
        self.label = Group( 
                        Rect(x+10, y+10,30, 30,fill='lightgrey'),
                        Label('N', x+25, y+25, size=24, fill=color),

                    )
        

class Queen():
    def __init__(self,color,x,y):
        self.color=color
        self.label = Group( 
                        Rect(x+10, y+10,30, 30,fill='lightgrey'),
                        Label('Q', x+25, y+25, size=24, fill=color),

                    )
        
        
class King():
    def __init__(self,color,x,y):
        self.color=color
        self.label = Group( 
                        Rect(x+10, y+10,30, 30,fill='lightgrey'),
                        Label('K', x+25, y+25, size=24, fill=color),

                    )
        


def translateXYtoBoard(x,y):
    return  y//50,x//50

def flip():
    for y in range(len(app.board)):
        app.board[y].reverse()
    app.board.reverse()

def movePawn(y_pos,x_pos, to_y_pos, to_x_pos):
    if (y_pos + 1 == to_y_pos and 
            x_pos == to_x_pos and
            app.board[to_y_pos][to_x_pos] == 0):
        return True
    elif (y_pos + 2 == to_y_pos and 
          y_pos == 1 and 
          x_pos == to_x_pos and
          app.board[to_y_pos][to_x_pos] == 0 and
          app.board[y_pos+1][x_pos] == 0):
        return True        
    elif (y_pos + 1 == to_y_pos and
          (x_pos - 1 == to_x_pos or x_pos + 1 == to_x_pos) and
          app.board[to_y_pos][to_x_pos] != 0 and
          app.board[y_pos][x_pos].color != app.board[to_y_pos][to_x_pos].color):
        return True
    return False

def moveRook(y_pos,x_pos, to_y_pos, to_x_pos):
    #four directions, only open space inbetween
    if (y_pos != to_y_pos and x_pos == to_x_pos):
        #check the spots inbetween
        if y_pos < to_y_pos:
            for y_spot in range(y_pos+1, to_y_pos, 1):
                if app.board[y_spot][x_pos] != 0:
                    return False

        elif y_pos > to_y_pos:
            for y_spot in range(y_pos-1, to_y_pos, -1):
                if app.board[y_spot][x_pos] != 0:
                    return False

    elif (x_pos != to_x_pos and y_pos == to_y_pos):
        #check the spots inbetween
        if x_pos < to_x_pos:
            for x_spot in range(x_pos+1, to_x_pos, 1):
                if app.board[y_pos][x_spot] != 0:
                    return False

        elif x_pos > to_x_pos:
            for x_spot in range(x_pos-1, to_x_pos, -1):
                if app.board[y_pos][x_spot] != 0:
                    return False
    else:
        return False
    return True
    
def moveBishop(y_pos,x_pos, to_y_pos, to_x_pos):
    if(abs(y_pos-to_y_pos)==abs(x_pos-to_x_pos)):
        if y_pos < to_y_pos and x_pos < to_x_pos:
            for pos in range(1,abs(y_pos-to_y_pos)):
                if app.board[y_pos+pos][x_pos+pos] != 0:
                    return False
        elif y_pos < to_y_pos and x_pos > to_x_pos:
            for pos in range(1,abs(y_pos-to_y_pos)):
                if app.board[y_pos+pos][x_pos-pos] != 0:
                    return False
        elif y_pos > to_y_pos and x_pos < to_x_pos:
            for pos in range(1,abs(y_pos-to_y_pos)):
                if app.board[y_pos-pos][x_pos+pos] != 0:
                    return False
        elif y_pos > to_y_pos and x_pos > to_x_pos:
            for pos in range(1,abs(y_pos-to_y_pos)):
                if app.board[y_pos-pos][x_pos-pos] != 0:
                    return False
    else:
        return False
    return True

def moveKnight(y_pos,x_pos, to_y_pos, to_x_pos):
    if((abs(y_pos-to_y_pos)==2 and abs(x_pos-to_x_pos)==1) or
           (abs(y_pos-to_y_pos)==1 and abs(x_pos-to_x_pos)==2) ):
        return True
    else:
        return False

def checkValidMove(y_pos,x_pos, to_y_pos, to_x_pos, x,y, turn):
    flipped = False
    if app.board[y_pos][x_pos].color != 'black':
        flip()
        y_pos = 7-y_pos
        x_pos = 7-x_pos
        to_y_pos = 7-to_y_pos
        to_x_pos = 7-to_x_pos
        flipped = True
    
    #pawn
    flag = False
    mid_flag = True
    if type(app.board[y_pos][x_pos]) is Pawn:
        mid_flag = movePawn(y_pos,x_pos, to_y_pos, to_x_pos)
        
    elif type(app.board[y_pos][x_pos]) is Rook:
        mid_flag = moveRook(y_pos,x_pos, to_y_pos, to_x_pos)

    elif type(app.board[y_pos][x_pos]) is Bishop:
        mid_flag = moveBishop(y_pos,x_pos, to_y_pos, to_x_pos)

    elif type(app.board[y_pos][x_pos]) is Knight:
        mid_flag = moveKnight(y_pos,x_pos, to_y_pos, to_x_pos)
    
    elif type(app.board[y_pos][x_pos]) is Queen:
        mid_flag = moveBishop(y_pos,x_pos, to_y_pos, to_x_pos)
        mid_flag = mid_flag or moveRook(y_pos,x_pos, to_y_pos, to_x_pos)
    
    elif type(app.board[y_pos][x_pos]) is King:
        if(abs(y_pos-to_y_pos)<=1 and abs(x_pos-to_x_pos)<=1):
            mid_flag = True
        else:
            mid_flag = False
    #check the destination spot
    if mid_flag:
        if app.board[to_y_pos][to_x_pos] == 0:
            flag = True
        elif app.board[y_pos][x_pos].color != app.board[to_y_pos][to_x_pos].color:
            #take
            flag = True
            if turn == 0 or turn == 2:
                app.board[to_y_pos][to_x_pos].label.visible = False
                app.board[to_y_pos][to_x_pos] = 0
                print('visible false',type(app.board[y_pos][x_pos]), y_pos,x_pos, to_y_pos, to_x_pos)

        
    if flag and (turn == 0 or turn == 2):
        app.board[y_pos][x_pos].label.centerX = x
        app.board[y_pos][x_pos].label.centerY = y
        app.board[y_pos][x_pos], app.board[to_y_pos][to_x_pos] = app.board[to_y_pos][to_x_pos], app.board[y_pos][x_pos]
        print(turn, type(app.board[to_y_pos][to_x_pos]), y_pos, x_pos, to_y_pos, to_x_pos)
        if flipped:
            flip()
        #the move was valid make the AI move
        if turn == 0:
            opponentMove()
    elif flag and turn == 1:
        return True
    else:
        return False


    
    
def opponentMove():
    #find all black pieces
    spots = []
    for y in range(8):
        for x in range(8):
            if (app.board[y][x] != 0 and 
               app.board[y][x].color == 'black'):
                   for y1 in range(8):
                       for x1 in range(8):
                            #find all valid moves
                            if checkValidMove(y,x,y1,x1, 0,0, 1):
                                spots.append((y,x, y1, x1))
    random.shuffle(spots)
    
    y, x, y1, x1 = spots[0]
    
    app.board[y][x].label.children[0].fill='pink'
    
    checkValidMove(y,x,y1,x1, x1*50+25,y1*50+25, 2)
    app.board[y1][x1].label.children[0].fill='lightgrey'

def onMousePress(x,y):
    y_pos, x_pos = translateXYtoBoard(x,y)
    print(app.board[y_pos][x_pos])
    if app.board[y_pos][x_pos] != 0:
        piece = app.board[y_pos][x_pos].label
        if piece.hits(x,y):
            if piece.children[0].fill != 'pink':
                piece.children[0].fill='pink'
            else:
                piece.children[0].fill='lightgrey'
    else:
        print('empty')

def findSelectedPiece():
    for row in range(8):
        for col in range(8):
            if app.board[row][col] != 0:
                if app.board[row][col].label.children[0].fill == 'pink':
                    x_pos = col
                    y_pos = row
                    return (col, row)
    return False
def onMouseRelease(x,y):
    result = findSelectedPiece()
    if result != False:
        x_pos, y_pos = result
        to_y_pos, to_x_pos = translateXYtoBoard(x,y)
        app.board[y_pos][x_pos].label.children[0].fill = 'lightgrey'
        checkValidMove(y_pos,x_pos, to_y_pos, to_x_pos,x,y, 0)
    print_board()
            
def print_board():
    for row in app.board:
        line = []
        for piece in row:
            if type(piece) is Pawn:
                line.append('P')
            elif type(piece) is Rook:
                line.append('R')
            elif type(piece) is Knight:
                line.append('N')
            elif type(piece) is Bishop:
                line.append('B')
            elif type(piece) is Queen:
                line.append('P')
            elif type(piece) is King:
                line.append('P')
            else:
                line.append('-')
        print(line)

def start():
    drawBoard()
    setBoard()

start()
cmu_graphics.run()