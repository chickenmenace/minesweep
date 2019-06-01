#!/usr/bin/python3

from board import *

game = minesweep_board()

game.print()
#game.print_open()
while game.game_status == minesweep_game_status.playing:
    row = input("Enter row or x to exit:")
    if row == 'x' or row == 'X':
        print('Bye!')
        quit()
    column = input("Enter column or x to exit:")
    if column == 'x' or column == 'X':
        print('Bye!')
        quit()
    game.play_cell(int(row),int(column))
    game.print()

if game.game_status == minesweep_game_status.won:
    print('Congratulations, you won!')
else:
    print('Boom! :(')

game.print_open()
