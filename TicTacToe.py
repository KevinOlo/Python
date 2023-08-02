import random as rand

board =["-", "-","-",
        "-","-","-",
        "-","-","-"]
currentP = 'X'
winner = None
gameRunning = True

#Print game board
def printBoard(board):
    print('\n')
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5 ])
    print('-----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('\n')

#printBoard(board)

#take player input

def playerin(board):
    inp = int(input('Enter a # 1-9: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentP
    else:
        print('Oops, try again')


#check 4 win or tie

def checkhoriz(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0] 
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3] 
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6] 
        return True
    
    
def checkrow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0] 
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1] 
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2] 
        return True
        
        
def checkdiag(board):
        global winner
        if board[0] == board[4] == board[8] and board[0] != '-':
            winner = board[0] 
            return True
        elif board[2] == board[4] == board[6] and board[2] != '-':
            winner = board[2] 
            return True    
        
def checktie(board):
        global gameRunning
        if '-' not in board:
            printBoard(board)
            print('Tie Game')
            gameRunning = False    

def checkwin():
    global gameRunning
    if checkdiag(board) or checkhoriz(board) or checkrow(board):
        printBoard(board)
        print(f'The winner is {winner}')
        gameRunning = False








#switch the player

def switchplayer():
    global currentP
    if currentP == 'X':
        currentP = 'O'
    else:
        currentP ='X'


#AI player
def computer(board):
    while currentP == 'O':
        position = rand.randint(0,8)
        if board[position] == '-':
            board[position] = 'O'
            switchplayer()




#check for win or tie again

while gameRunning:
    printBoard(board)
    playerin(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    if winner == None:
        checktie(board)