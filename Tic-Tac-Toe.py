import random

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        #player chooses letter first
        print('Which letter would you like to be?')
        input().upper()
        #now the computer gets the other letter
    if letter == 'X':
        return ['X', 'O'] # rationalle for two values in the returned list.  
                            # The followoing code is found later on, 
                            # requiring two inputs:
                            # playerLetter, computerLetter = inputPlayerLetter()
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0
        return 'Player'
    else:
        return 'Computer'

def makeMove(board, letter, move):
    board[move] = letter    #this changes the board list at [index] to the letter passed

def isWinnter(bo, le):  #bo and le are short for board and letter
        return
            (bo[7] == le and bo[8] == le and bo[9] == le) or    #top
            (bo[4] == le and bo[5] == le and bo[6] == le) or    #across middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or    #bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or    #left
            (bo[5] == le and bo[8] == le and bo[2] == le) or    #down middle
            (bo[3] == le and bo[6] == le and bo[9] == le) or    #right
            (bo[7] == le and bo[5] == le and bo[3] == le) or    #diagonal top left to bottom right
            (bo[1] == le and bo[5] == le and bo[9] == le) or    #diagonal top right to bottom left
            )