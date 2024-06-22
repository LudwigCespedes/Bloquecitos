import heapq
from collections import deque
#from piece import *



class Board:
    """
    Class representing the Blokus game board.
    Attributes:
    - row: Number of rows in the board.
    - col: Number of columns in the board.
    - board: 2D list representing the current state of the board, initialized with '■'.
    - piece: Empty dictionary to store pieces.
    - corners: List of corner positions on the board.
    - players_pieces: Dictionary storing positions occupied by each player.

    """
    
    def __init__(self, size):

        """
        Initializes a Board object with a board of size 'size x size'.

        Parameters:
        - size: Size of the board (same number of rows and columns).
        """

        self.row = size
        self.col = size
        self.board = [['■' for _ in range(self.col)] for _ in range(self.row)]
        self.piece = {}
        self.corners = [(0, 0), (0, self.col - 1), (self.row - 1, 0), (self.row - 1, self.col - 1)]
        self.players_pieces = {}    

    def place_piece(self, piece, position, player):
        if not self.is_valid_placement(piece, position, player):
            return False

        x, y = position
        for i, row in enumerate(piece):
            for j, value in enumerate(row):
                if value != '■':
                    self.board[x + i][y + j] = str(value)
                    if player.name not in self.players_pieces:
                        self.players_pieces[player.name] = []
                    self.players_pieces[player.name].append((x + i, y + j))
        
        piece_tuple = tuple(tuple(row) for row in piece)
        piece_tuple1 =tuple(tuple(row) for row in player.mirror_piece(piece))
        piece_tuple2 = tuple(tuple(row) for row in player.transpose_piece(piece))
        player.used_pieces.add(piece_tuple)
        player.used_pieces.add(piece_tuple1)
        player.used_pieces.add(piece_tuple2)
        return True
    
    def is_valid_placement(self, piece, position, player):
        piece_tuple = tuple(tuple(row) for row in piece)
        if piece_tuple in player.used_pieces:
            #print("Pieza ya utilizada")
            return False

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

        """
        Returns the movable pieces available for a given player along with their valid positions.

        Parameters:
        - player: Player object for which to determine movable pieces.

        Returns:
        - List of tuples (piece number, piece, valid position).
        """

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

        """
        Calculates player scores based on occupied positions on the board.

        Returns:
        - Dictionary where keys are player names and values are their scores.
        """

        scores = {}
        total = 89
        for player in self.players_pieces:
            remaining_squares = len(self.players_pieces[player])
            scores[player] = total-remaining_squares
        return scores
    def display_board(self):
        """
        Displays the board in the console.
        """        
        for row in self.board:
            print(' '.join(row))

    def __repr__(self):
        """
        Returns a string representation of the board.
        """
        return '\n'.join([' '.join(row) for row in self.board])


