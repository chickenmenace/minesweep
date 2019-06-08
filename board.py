from enum import Enum
class minesweep_game_status(Enum):
    playing = 0
    won = 1
    lost = 2

    

class minesweep_board:
    from collections import Set
    
    
    def __init__(self, board_lenght = 15, board_height = 15, mines = 15):
        from random import shuffle
        
        #initialize board
        self.board_lenght = board_lenght
        self.board_height = board_height
        self.mines = mines
        self.board = [0] * board_height * board_lenght
        self.played_cells = set()
        for i in range(mines):
            self.board[i] = "+"
        for n in range(1000):
            shuffle(self.board)
        self._populate_numbers()
        self.game_status = minesweep_game_status.playing

    def play_cell(self,row, column):
        cell_number = row * self.board_lenght + column
        if cell_number in self.played_cells:
            print('Move not allowed - cell is already open')
            return False

        self.played_cells.add(cell_number)

        #Check if mine
        if self.board[cell_number] == '+':
            print('Boom!')
            self.board[cell_number] = '☠'
            self.game_status = minesweep_game_status.lost
            self.print_open
            return
        
        if self.board[cell_number] == 0:
            # found empty, check neighbors
            zero_cells = set()
            zero_cells.add(cell_number)
            
            while len(zero_cells) > 0:
                current = zero_cells.pop()
                self.played_cells.add(current)
                for c in self.get_neighbor_cells(current):
                    if c not in self.played_cells:
                        if self.board[c] == 0:
                            zero_cells.add(c)
                        else:
                            self.played_cells.add(c)
                

        if len(self.played_cells) == len(self.board) - self.mines:
            self.game_status = minesweep_game_status.won

        return True

    def get_neighbor_cells(self, cell):
        neighbor_cells = set()
        #North 
        try_cell = cell - self.board_lenght
        if try_cell >= 0:
            neighbor_cells.add (try_cell)
            #North-East
            if try_cell % self.board_lenght + 1 < self.board_lenght:
                neighbor_cells.add(try_cell + 1)
            #North-West
            if try_cell % self.board_lenght > 0:
                neighbor_cells.add(try_cell - 1)

        #South
        try_cell = cell + self.board_lenght

        if (try_cell) < len(self.board) :
            neighbor_cells.add (try_cell)
            #South-East
            if try_cell % self.board_lenght + 1 < self.board_lenght:
                neighbor_cells.add(try_cell + 1)
            #South-West
            if try_cell % self.board_lenght  > 0:
                neighbor_cells.add(try_cell - 1)

        #East
        if (cell % self.board_lenght + 1 < self.board_lenght):
            neighbor_cells.add (cell + 1)

        #West
        if (cell % self.board_lenght > 0):
            neighbor_cells.add (cell - 1)

        return neighbor_cells  
        #S = cell + self.board_height



    def _populate_numbers(self):
        for i in range(len(self.board)):
            count = 0
            if self.board[i] == 0:
                for n_cell in self.get_neighbor_cells(i):
                    if self.board[n_cell] == '+':
                        count += 1
                self.board[i] = count    



    def print_raw(self):
        for i in range(len(self.board)):
            if i % self.board_lenght == 0:
                print ('\n', end = '')        
            print (self.board[i], end = '')
        print ('\n')
    
    def print(self):
        if self.board_height > 10:
            print ('   ', end='')
        else:
            print ('  ', end='')
        for i in range(0,self.board_lenght):
            if self.board_lenght > 10:
                if i > 9:
                    print('' + str(i) + ' ' ,end = '')
                else:
                    print(' ' + str(i) + ' ' ,end = '')
            else:
                print(' ' + str(i) + ' ' ,end = '')
        if self.board_height > 10:
            print ('\n  ╔', end='')
        else:
            print ('\n ╔', end='')
        for i in range(0,self.board_lenght):
            print('═══' ,end = '')
        for i in range(len(self.board)):
            if self.board_height < 11:
                if i % self.board_lenght == 0:
                    if i == 0 :
                        print ( '╗\n' + str(int(i/self.board_lenght)) + '║', end = '')
                    else:
                        print ( '║\n' + str(int(i/self.board_lenght)) + '║', end = '')
                if i in self.played_cells:
                    if self.board[i] == 0:
                        print ('   ', end='')
                    else:
                        print (' ' + str(self.board[i]) + ' ', end='')
                else:
                    print (' \u25A1 '  , end = '') #u25A1 1360 1368 13EB 1CC0 1CC1 203B 2055 205C 235F 233E 2600 2606 _2620 2622 2623
            else:

                if i % self.board_lenght == 0:
                    if i == 0 :
                        print ( '╗\n' + ' ' + str(int(i/self.board_lenght)) + '║', end = '')
                    elif int(i/self.board_lenght) < 10:
                        print ( '║\n' + ' ' + str(int(i/self.board_lenght)) + '║', end = '')
                    elif int(i/self.board_lenght) > 9:
                        print ( '║\n' + str(int(i/self.board_lenght)) + '║', end = '')
                if i in self.played_cells:
                    if self.board[i] == 0:
                        print ('   ', end='')
                    else:
                        print (' ' + str(self.board[i]) + ' ', end='')
                else:
                    print (' \u25A1 '  , end = '')
        if self.board_height > 10:
            print ('║\n  ╚', end='')
        else:
            print ('║\n ╚', end = '')
        for i in range(0,self.board_lenght):
            print('═══' ,end = '')  
        print ('╝\n')  
    def print_open(self):
        if self.board_height > 10:
            print ('   ', end='')
        else:
            print ('  ', end='')
        for i in range(0,self.board_lenght):
            if self.board_lenght > 10:
                if i > 9:
                    print('' + str(i) + ' ' ,end = '')
                else:
                    print(' ' + str(i) + ' ' ,end = '')
            else:
                print(' ' + str(i) + ' ' ,end = '')
        if self.board_height > 10:
            print ('\n  ╔', end='')
        else:
            print ('\n ╔', end='')
        for i in range(0,self.board_lenght):
            print('═══' ,end = '')
        for i in range(len(self.board)):
            if i % self.board_lenght == 0:
                if self.board_height <= 10:
                    if i == 0 :
                        print ( '╗\n' + str(int(i/self.board_lenght)) + '║', end = '')
                    else:
                        print ( '║\n' + str(int(i/self.board_lenght)) + '║', end = '')
                   # print ('\n' + str(int(i/self.board_lenght)) + '║', end = '')
                else:
                    if i == 0:
                        print ( '╗\n ' + str(int(i/self.board_lenght)) + '║', end = '')
                    elif int(i/self.board_lenght) < 10:
                        print ('║\n ' + str(int(i/self.board_lenght)) + '║', end = '')
                    else:
                        print ('║\n' + str(int(i/self.board_lenght)) + '║', end = '')
            if self.board[i] == 0:
                print ('   ', end='')
            else:
                print (' ' + str(self.board[i]) + ' ', end='')
        if self.board_height > 10:
            print ('║\n  ╚', end='')
        else:
            print ('║\n ╚', end = '')
        for i in range(0,self.board_lenght):
            print('═══' ,end = '')  
        print ('╝\n')
