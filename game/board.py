import heapq
from collections import deque

class Piece:
    """
    A class for modeling a car 
    """
    def __init__(self, id, length, ):
        self.id = id
        self.length = length



class Board:
    def __init__(self, size):
        self.row = size
        self.col = size
        self.board = [['.' for _ in range(self.col)] for _ in range(self.row)]
        self.pi = {}


    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def __repr__(self):
        return str(self.board)


