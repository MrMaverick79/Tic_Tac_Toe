# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 14:47:46 2021
Plays a game of tic tac toe using TEXT

@author: Brendan Tuckerman
"""

# Plays a game of tic tac toe
gameover= False
moves = 0

# Create a dictionary which will hold the values of either x or o
myboard = {
    'top-l': ' ',
    'top-m': ' ', 
    'top-r': ' ', 
    'mid-l': ' ', 
    'mid-m': ' ', 
    'mid-r' : ' ',
    'bottom-l' : ' ',
    'bottom-m' : ' ', 
    'bottom-r' : ' ',
 }

class play_game():

    def __init__(self, board):

        self.board =myboard

    def showBoard(board):
        """ creates a printable board"""
        print('\n\n')
        print(myboard['top-l'] + '|' + myboard['top-m'] + '|' \
              + myboard['top-r'])
        print('-----')
        print(myboard['mid-l'] + '|' + myboard['mid-m'] + '|' + \
              myboard['mid-r'])
        print('-----')
        print(myboard['bottom-l'] + '|' + myboard['bottom-m'] + '|' \
            + myboard['bottom-r'])
        print('\n\n')
  


    def winconditions():

        # Checks to see whether you have won
        global gameover
        if (myboard['top-l'] == 'x' \
            and myboard['top-m'] == 'x' \
            and myboard['top-r']) == 'x':
            print('You win!')
            gameover = True
        elif (myboard['mid-l'] == 'x'\
            and myboard['mid-m'] == 'x'\
            and myboard['mid-r']) == 'x':
            print('You win!')
            gameover = True
        elif (myboard['bottom-l'] == 'x'\
            and myboard['bottom-m'] == 'x'\
            and myboard['bottom-r']) == 'x':
            print('You win!')
            gameover = True        
        elif (myboard['top-l'] == 'x' \
            and myboard['mid-l'] == 'x'\
            and myboard['bottom-l']) == 'x':
            print('You win!')
            gameover = True        
        elif (myboard['top-m'] == 'x'\
            and myboard['mid-m'] == 'x'\
            and myboard['bottom-m']) == 'x':
            print('You win!')
            gameover = True
        elif (myboard['top-r'] == 'x'\
            and myboard['mid-r'] == 'x'\
            and myboard['bottom-r']) == 'x':
            print('You win!')
            gameover = True
        elif (myboard['top-r'] == 'x'\
            and myboard['mid-m'] == 'x'\
            and myboard['bottom-l']) == 'x':
            print('You win!')
            gameover = True
        elif (myboard['top-l'] == 'x'\
            and myboard['mid-m'] == 'x'\
            and myboard['bottom-r']) == 'x':
            print('You win!')
            gameover = True

    def lose_conditions():
        # Checks to see whether you have lost.
        global gameover
        if (myboard['top-l'] == 'o') and \
           (myboard['top-m'] == 'o') and \
           (myboard['top-r'] == 'o'):
            gameover = True
        elif (myboard['mid-l']) == 'o'\
            and (myboard['mid-m']) =='o'\
            and (myboard['mid-r']) == 'o':
            gameover = True
        elif (myboard['bottom-l'] == 'o'and myboard['bottom-m'] == 'o' \
            and myboard['bottom-r']) == 'o':
            gameover = True
        
        elif (myboard['top-l'] == 'o' and myboard['mid-l'] == 'o' \
            and myboard['bottom-l']) == 'o':
            gameover = True
        
        elif (myboard['top-m'] == 'o' and myboard['mid-m'] == 'o' and \
            myboard['bottom-m']) == 'o':
            gameover = True
            
        elif (myboard['top-r'] == 'o' and myboard['mid-r'] == 'o' \
            and myboard['bottom-r']) == 'o':
            gameover = True
            

        elif (myboard['top-r'] == 'o' and myboard['mid-m'] == 'o' \
            and myboard['bottom-l']) == 'o':
            
            gameover = True
        elif myboard['top-l'] == 'o' and myboard['mid-m'] == 'o' and \
            myboard['bottom-r'] == 'o':
            gameover = True
        

    def player_move():
        # The user selects a move
        move = input('Where would you like to go? \nul / um / ur'
            '\nml / mm / mr \nbl / bm / br?')
        if move == 'ul':
            myboard['top-l'] = 'x'
        elif move == 'um':
            myboard['top-m'] = 'x'
        elif move == 'ur':
            myboard['top-r'] = 'x'
        elif move == 'ml':
            myboard['mid-l'] = 'x'
        elif move == 'mm':
            myboard['mid-m'] = 'x'
        elif move == 'mr':
            myboard['mid-r'] = 'x'
        elif move == 'bl':
            myboard['bottom-l'] = 'x'
        elif move == 'bm':
            myboard['bottom-m'] = 'x'
        elif move == 'br':
            myboard['bottom-r'] = 'x' 
        else:
            print('\nThat is not a valid move!')   

                   
    def ai_move():
        # oppostion moves... AI is a bit rich!
        # AI always chooses middle where possible     
        if myboard['mid-m'] != 'x' and myboard['mid-m']!= 'o':
            myboard['mid-m'] = 'o'
           
        elif myboard['top-r'] != 'x' and myboard['top-r'] != 'o':
            myboard['top-r'] = 'o'
            
         # These are the non ai moves   
        elif myboard['top-l'] != 'x'and myboard['top-l'] != 'o':
             myboard['top-l'] = 'o'
            
        elif myboard['bottom-r'] != 'x' and myboard['bottom-r'] != 'o':
             myboard['bottom-r'] = 'o'
            
        elif myboard['bottom-l'] != 'x' and myboard['bottom-l'] != 'o':
             myboard['bottom-l'] = 'o'
            
        elif myboard['top-m'] != 'x' and myboard['top-m'] != 'o':
             myboard['top-m'] = 'o'
            
        elif myboard['mid-l'] != 'x' and myboard['mid-l'] != 'o':
             myboard['mid-l'] = 'o'
            
        elif myboard['mid-r'] != 'x' and  myboard['mid-r'] != 'o':
             myboard['mid-r'] = 'o'
            
        elif myboard['bottom-m'] != 'x' and myboard['bottom-m'] != 'o':
             myboard['bottom-m'] = 'o'
            

# Run the game
# determine whether the game is active
while gameover == False:
    # show the board
    play_game.showBoard(myboard)

    # player moves
    play_game.player_move()

    #show the new board
    play_game.showBoard(myboard)
    
    #check to see if the player wins 
    # and checks on whether the player wants another game
    play_game.winconditions()
    moves +=1
    
    if gameover == True:
        print(f'Congratulations! You won in {moves} moves.')
        moves = 0
        for keys in myboard:
                myboard[keys] = ' '
        another = input('Would you like to play again?(y/n):')
        if another == 'y':                
            gameover = False
           
   # AI moves 
    if moves != 0:
        play_game.ai_move()
       
    # Check to see whether AI wins
        play_game.lose_conditions()
        if gameover == True:
            moves = 0
            for keys in myboard:
                myboard[keys] = ' '
                another = input('Would you like to play again?(y/n):')
                if another == 'y':                
                    gameover = False
                
                