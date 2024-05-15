# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:23:54 2024

@author: Zia
"""
def createBoard():
    #using lists
    board = ['_', '_', '_',
             '_', '_', '_',
             ' ', ' ', ' ']
    return board

def changeBoard(board, move):
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])

    
def playerOne(board):
    move = int(input('Player One: please give a number 1-9:\n'))
    if move > 9: 
        print('This number is too large')
        move = int(input('Player One: please give a number 1-9:\n'))
 
    
    elif board[move] != '_' and board[move] != ' ':
        print('This is not a free space')
        move = int(input('Player One: please give a number 1-9:\n'))


    board[move] = 'x'
    return board
    
def playerTwo(board):
    move = int(input('Player Two: please give a number 1-9:\n'))
    if move > 9: 
        print('This number is too large')
        move = int(input('Player Two: please give a number 1-9:\n'))
 
    
    elif board[move] != '_' and board[move] != ' ':
        print('This is not a free space')
        move = int(input('Player Two: please give a number 1-9:\n'))


    board[move] = 'o'
    return board

#board spaces
# 0|1|2
# 3|4|5
# 6|7|8

def checkRows(board):
    if board[0] == board[1] == board[2] and board[0] != '-':
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        return True
    elif board[6] == board[7] == board[8] and board[6] != ' ':
        return True
    else:
        return False
    
def checkColumn(board):
    if board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    else:
        return False
    
def checkDiagonal(board):
    if board[0] == board[4] == board[8]:
        return True
    elif board[6] == board[4] == board[2]:
        return True
    else: 
        return False
    
def checkTie(board):
    for i in range(len(board)):
        if board[i] == '-' or ' ':
            return False
        else:
            return True
        
def checkWinner(row, column, diagonal, tie):
    if row == column == diagonal == tie == True:
        return True
    else: 
        return False
    
def main():
    winner = None
    game = 
#start game 
    board = createBoard()
    move = 1
    changeBoard(board,move)
    
    while 
        move1 = playerOne(board)
        changeBoard(board, move1)
        print()
    
        move2 = playerTwo(board)
        changeBoard(board, move2)
        print()
        
        
    print('game over')
main()