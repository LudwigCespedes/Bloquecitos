import heapq
from collections import OrderedDict
import copy
#from piece import *



class Board:
        
    def __init__(self, size):
    # Se inicializa un tablero size x size

        self.row = size # Numero de filas en el tablero
        self.col = size # Numero de columnas en el tablero
        self.board = [['■' for _ in range(self.col)] for _ in range(self.row)]
        self.piece = {} # Diccionario vacio para almacenar las piezas
        self.corners = [(0, 0), (0, self.col - 1), (self.row - 1, 0), (self.row - 1, self.col - 1)] # Lista de posiciones de las esquinas en el tablero 
        #NO TOCAR
        self.players_pieces = {} # Diccionario que almacena las pociones ocupadas por cada jugador
        #self.piezas
        self.jugadores = [] # objetos player

 

# Colocacion de pieza en el tablero 

    def place_piece(self, piece, position, player):

        # Piece, pieza a colocar en el tableor
        # Position, poscicion donde se colocara
        # Player, jugdor que coloca la pieza
        if not self.is_valid_placement(piece, position, player):
            return False

        x, y = position
        for i, row in enumerate(piece):
            for j, value in enumerate(row):
                if value != '■':
                    self.board[x + i][y + j] = str(value)
                    if player.name not in self.players_pieces:
                        self.players_pieces[player.name] = []
                        self.jugadores.append(player)
                    self.players_pieces[player.name].append((x + i, y + j))
                    self.jugadores.append(player)
        
        piece_list =  player.all_transpositions(piece)

        player.used_pieces.extend(piece_list)
        player.puntos_piezas.append(piece_list)

        return True
    
 # Verificacion de la pieza en la posicion 

    def is_valid_placement(self, piece, position, player):

        # piece, la pieza
        # position, la posicion 
        # player, el jugador

        piece_tuple = piece
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
    


# Lista de las piezas disponibles para jugar con sus movimientos disponibles tambien

    def get_movable_pieces(self, player):

        #player, jugador

        movable_pieces = []
        for index, piece in enumerate(player.get_pieces()):
            for x in range(self.row):
                for y in range(self.col):
                    if self.is_valid_placement(piece, (x, y), player):
                        movable_pieces.append((index + 1, piece, (x, y)))
                        break 
        # Lista de tupla (Numero de pieza, pieza, posicion valida)
        return movable_pieces
    


    
    def cal_culo_de_puntos (self,player = False):
        puntos = {}
        cul = 0
        total = 89
        if player:
            for piece in player.puntos_piezas:
                cul = cul + self.heuristic_use_large_pieces_first(piece[0])
            puntos[player.name]=total-cul
            ganadores = OrderedDict(sorted(puntos.items(), key=lambda x: x[1]))
            return ganadores  

        for jugador in self.jugadores:
            cul = 0
            for piece in jugador.puntos_piezas:
               cul = cul + self.heuristic_use_large_pieces_first(piece[0])
            puntos[jugador.name]=total-cul

        ganadores = OrderedDict(sorted(puntos.items(), key=lambda x: x[1]))
        return ganadores  
    
                    
    def cal_culo_de_puntos1 (self,player = False):

        cul = 0

        if player:
            for piece in player.puntos_piezas:
                cul = cul + self.heuristic_use_large_pieces_first(piece[0])
        
            return cul

        for jugador in self.jugadores:
            cul = 0
            for piece in jugador.puntos_piezas:
               cul = cul + self.heuristic_use_large_pieces_first(piece[0])

        return cul

    
    def heuristic_use_large_pieces_first(self,matrix):

        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '■':
                    count= count + 1
        return count
    
    
    
# Muestra el tablero en la consola 

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

# Representacion en cadena del tablero

    def __repr__(self):

        return '\n'.join([' '.join(row) for row in self.board])


