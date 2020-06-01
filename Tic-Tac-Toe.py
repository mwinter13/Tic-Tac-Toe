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

