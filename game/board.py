import heapq
from collections import deque
#from piece import *



class Board:

    
    def __init__(self, size):
        self.row = size
        self.col = size
        self.board = [['■' for _ in range(self.col)] for _ in range(self.row)]
        self.piece = {}
        self.corners = [(0, 0), (0, self.col - 1), (self.row - 1, 0), (self.row - 1, self.col - 1)]
        self.players_pieces = {}    

    def place_piece(self, piece, position, player):
        if not self.is_valid_placement(piece, position, player):
            print("Movimiento inválido")
            return False
        
        x, y = position
        for i, row in enumerate(piece):
            for j, value in enumerate(row):
                if value != '■':
                    self.board[x + i][y + j] = str(value)
                    if player.name not in self.players_pieces:
                        self.players_pieces[player.name] = []
                    self.players_pieces[player.name].append((x + i, y + j))
        return True
    
    def is_valid_placement(self, piece, position, player):
        x, y = position
        is_first_move = not player.name in self.players_pieces
        touches_corner = any([(x + i, y + j) in self.corners for i, row in enumerate(piece) for j, value in enumerate(row) if value != '■'])
        
        if is_first_move and not touches_corner:
            return False
        
        if not is_first_move:
            touches_corner_of_own_piece = any([
                (x + i + dx, y + j + dy) in self.players_pieces[player.name]
                for i, row in enumerate(piece)
                for j, value in enumerate(row)
                if value != '■'
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            ])
            touches_side_of_own_piece = any([
                (x + i + dx, y + j + dy) in self.players_pieces[player.name]
                for i, row in enumerate(piece)
                for j, value in enumerate(row)
                if value != '■'
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            ])
            if not touches_corner_of_own_piece or touches_side_of_own_piece:
                return False

        for i, row in enumerate(piece):
            for j, value in enumerate(row):
                if value != '■':
                    if x + i < 0 or x + i >= self.row or y + j < 0 or y + j >= self.col:
                        return False
                    if self.board[x + i][y + j] != '■':
                        return False
        return True
    
    def place_piece1(self, piece,position):
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


    def get_movable_pieces(self, player):
        movable_pieces = []
        for index, piece in enumerate(player.get_pieces()):
            for x in range(self.row):
                for y in range(self.col):
                    if self.is_valid_placement(piece, (x, y), player):
                        movable_pieces.append((index + 1, piece, (x, y)))
                        break 
        return movable_pieces
    def find_valid_moves(self, piece, player):
        valid_moves = []
        for x in range(self.row):
            for y in range(self.col):
                if self.is_valid_placement(piece, (x, y), player):
                    valid_moves.append((x, y))
        return valid_moves
                    
    def calculate_scores(self):
        scores = {}
        total = 89
        for player in self.players_pieces:
            remaining_squares = len(self.players_pieces[player])
            scores[player] = total-remaining_squares
        return scores
    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def __repr__(self):
        return str(self.board)


