import heapq
from collections import deque



class Board:

    
    def __init__(self, size):
        self.row = size
        self.col = size
        self.board = [['■' for _ in range(self.col)] for _ in range(self.row)]
        self.piece = {}

    def place_piece(self, piece,position):
        x, y =position
        for i, row in enumerate(piece):
            for j, value in enumerate(row):
                if value == 1:
                    self.board[x+i][y+j]= "1"
                elif value == 2:
                    self.board[x+i][y+j]= "2"
                elif value == 3:
                    self.board[x+i][y+j]= "3"
                elif value == 4:
                    self.board[x+i][y+j]= "4"
                else:
                    print("no DE BOARD")
                

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def __repr__(self):
        return str(self.board)


