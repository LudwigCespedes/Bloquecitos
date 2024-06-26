import time
import pandas as pd
import os
import tracemalloc
import copy
import random
from collections import deque
import heapq
from collections import OrderedDict


# Clase que representa los boots y el minimax

class Bots:

    def __init__(self):

        self.max_depth = 1
        self.max_time = 100000

# BOT ALEATORIO 

    def bot_aleatorio(self,board,player):

        state = copy.deepcopy(board)
        try:
            frontier = state.get_movable_pieces(player)
            current_state= random.choice(frontier)
        except:
            #print(len(frontier))
            print(f"El jugador {player.name} no tiene más piezas para jugar. Pasando el turno...")
            return state   # Devuelve el estado actual del tablero sin realizar ningún movimiento
        
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],player)
        #state.display_board() 

        # Nuevo estado del tablero despues del movimiento
        self.board = copy.deepcopy(state)     
        return state
       
# BOT GREEDY

    def bot_greedy(self,board,player):
        
        state = copy.deepcopy(board)
        try:
            frontier = self.add_heuristic_value(state.get_movable_pieces(player),player,board)
            current_state= max(frontier, key=lambda x: x[0])
            
        except:
            #print(frontier)
            print(f"El jugador {player.name} no tiene más piezas para jugar. Pasando el turno...")
            return state  # Devuelve el estado actual del tablero sin realizar ningún movimiento
        
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],player)


        # Nuevo estado del tablero despues del movimiento 
        self.board = copy.deepcopy(state)     
        return state
    

# BOT PEORES DECISIONES

    def bot_peores_decisiones(self,board,player):

        state = copy.deepcopy(board)
        try:
            frontier = self.add_heuristic_value(state.get_movable_pieces(player),player,board)
            current_state= min(frontier, key=lambda x: x[0])
        except:
            #print(len(frontier))
            print(f"El jugador {player.name} no tiene más piezas para jugar. Pasando el turno...")
            return state  # Devuelve el estado actual del tablero sin realizar ningún movimiento
        
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],player)
        #state.display_board()

        # Nuevo estado del tablero despues del movimiento
        self.board = copy.deepcopy(state)       
        return state
    
# Primera heuristica

    def heuristic_use_large_pieces_first(self,matrix):

        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '■':
                    count= count + 1
        return count


    # Segunda heuristica

    def heuristic_player_mobility(self,player,board):
        mobility_score = len(board.get_movable_pieces(player))
        #print(mobility_score)
        return mobility_score
    
    # Tercera heuristica

    def heuristic_proximity_to_corner(self, matrix):
        count = 0
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        
        if rows == 0 or cols == 0:
            return count

        corners = [(0, 0), (0, cols-1), (rows-1, 0), (rows-1, cols-1)]
        proximity_range = 2  # piezas dentro de 2 celdas de las esquinas

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != '■':
                    for corner in corners:
                        if abs(corner[0] - i) <= proximity_range and abs(corner[1] - j) <= proximity_range:
                            count += 1
                            break  # Solo cuenta una vez por pieza
       
        return count
    
    # Cuarta heuristica


    def heuristic_minimize_opponent_pieces(self, player,player_name ):
            
        
            for jugador in self.jugadores:
                    if jugador.name != player_name:
                        opponent_name = (player_name)
                    opponent_moves = sum(1 for move in self.get_movable_pieces(opponent_name(player)))
                    print(opponent_moves)
            return len(self.players_pieces[opponent_moves])

    # Quinta heuristica
    
    def heuristic_control_borders(self, player, board):
        border_pieces = 0
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == player:
                    if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                        border_pieces += 1
                        
        return border_pieces


    """
    def heuristic_block_opponents(self, piece, board, opponent, player):
        # Heurística para evaluar cuántas posiciones del oponente se bloquean con la pieza actual.
        blocked_positions = 0
        for move in board.get_movable_pieces(piece):
            if move in opponent.positions:
                blocked_positions += 1
        return blocked_positions


    def heuristic_control_center(self, piece, board):
        center_x, center_y = 10,10
        piece_x, piece_y = piece.position
        distance_to_center = abs(center_x - piece_x) + abs(center_y - piece_y)
        return max(0, board.max_distance - distance_to_center)
    


"""

# Heuristica del minimax
    

    def heuristic_cal_culo_de_puntos (self):
        puntos = {}
        culo = 0
        for jugador in self.jugadores:
            culo = 0
            for piece in jugador.puntos_piezas:
               culo = culo + self.heuristic_use_large_pieces_first(piece[0])
            puntos[jugador.name]=culo

        ganadores = OrderedDict(sorted(puntos.items(), key=lambda x: x[1]))
        return ganadores  
    

    

# Agregacion de valores heuristicos a las piezas moviles
    
    def add_heuristic_value(self, get_movable_pieces,player,board):
        new_get_movable_pieces = []

        for get_movable in get_movable_pieces:
            value = self.combined_heuristics(get_movable[1],player, board)
            new_get_movable_pieces.append((value, get_movable[1], get_movable[2]))
        
        return new_get_movable_pieces
    
# Normalizacion de los valores heuristicos al rango de [0, 1]

    def min_max_normalization(self,values):

        min_val = min(values)
        max_val = max(values)
        
        return [(x - min_val) / (max_val - min_val) for x in values]    


# Combinacion de las heuristicas para obtener un valor heuristico combinado

    def combined_heuristics(self, pieces, player,board, heuristics=['heuristic_use_large_pieces_first']):
        total_cost = []
        
        for heuristic in heuristics:
            if heuristic == 'heuristic_use_large_pieces_first':
                max1 = 5
                total_cost.append((self.heuristic_use_large_pieces_first(pieces) + 0.1) / max1)
            elif heuristic == 'heuristic_proximity_to_corner':
                max2 = 4  
                total_cost.append((self.heuristic_proximity_to_corner(pieces) + 0.1) / max2)
            elif heuristic == 'heuristic_minimize_opponent_pieces':
                max3 = 10
                total_cost.append((self.heuristic_minimize_opponent_pieces(pieces,board.jugadores[-1]) + 0.1) / max3)
            elif heuristic == 'heuristic_control_borders':
                max4 = 4
                total_cost.append((self.heuristic_control_borders(player,board) + 0.1) / max4)
            elif heuristic == 'heuristic_player_mobility':
                max5 = 168
                total_cost.append((self.heuristic_player_mobility(player,board) + 0.1) / max5)

        
        resultado = sum(total_cost)
        return resultado # Suma de valores heuristicos

       


# Cuenta las esquinas de una matriz donde hay valores no vacios


    def count_corners(self,matrix):

        count = 0
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        
        if rows < 2 or cols < 2:
            return 0
        
        if matrix[0][0] != '■':  # Esquina superiror izquierda
            count += 1
        if matrix[0][cols-1] != '■':  # Esquina superior derecha
            count += 1
        if matrix[rows-1][0] != '■':  # Esquina inferior izquierda
            count += 1
        if matrix[rows-1][cols-1] != '■':  # Esquina inferior derecha
            count += 1
        
        # El numero de esquinas con valores no vacios
        return count
    
    def _max(self):
        pass
    def _mini(self):
        pass
    
        
# LAS METRICAS

    def metricas(ganador, puntos, tiempo_ejecucion, memoria_actual, memoria_maxima):
        

        # Ganador: Nombre del ganador
        # Puntos: Puntos obtenidos por el jugador
        # Tiempo_ejecucion: Tiempo total de ejecucion del juego 
        # Memoria_actual: Uso actual de memoria durante el juego 
        # Memoria_maxima: Pico maximo de uso de memoria durante el juego
        # Ruta: Ruta tomada
        # Tamano_de_la_ruta: Numero de acciones

        if os.path.exists("..","metricas.csv"):
            df = pd.read_csv("..","metricas.csv")
        else:
            df = pd.DataFrame(columns=["ganador", "puntos", "tiempo_ejecucion", "memoria_actual", "memoria_maxima"])
        
        # Crear un nuevo DataFrame con los datos a agregar
        nuevo_dato = pd.DataFrame([{
            "ganador": ganador, 
            "puntos": puntos, 
            "tiempo_ejecucion": tiempo_ejecucion, 
            "memoria_actual": memoria_actual, 
            "memoria_maxima": memoria_maxima
        }])
        
        
        df = pd.concat([df, nuevo_dato], ignore_index=True)
        
        df.to_csv("metricas.csv", index=False)
        
        print(f"Archivo 'metricas.csv' actualizado con éxito.")

    def is_terminal(self,board,player):
        # Define si el estado es terminal (si el juego ha terminado)
        tabla = copy.deepcopy(board)
        #for player in tabla.jugadores:
        #print(tabla.get_movable_pieces(player))
        if tabla.get_movable_pieces(player):
            return False
            
        return True
    def children1(self,board,player):
        tabla = copy.deepcopy(board)
        options = tabla.get_movable_pieces(player)
        children = []
        for option in options:
            child = copy.deepcopy(board)
            new_player = copy.deepcopy(player)
            child.place_piece(option[1], option[2],new_player)
            #print(len(new_player.used_pieces))
            #len(child.p)
            #child.remove
            children.append([option,child,new_player])
            #children.append(child)

        return children


    def solve(self, state, player,players):
        self.start_time = time.time()
        for depth in range(2):
            try:
                best_option, _ = self.maximize(state, player, float("-inf"), float("inf"), depth,players)
            except StopIteration:
                break

        return best_option

    def maximize(self, board, player, alfa, beta, depth,players):
        if self.should_stop(board, player, depth):
            return None, self.evaluate1(board, player)
        
        max_child, max_utility = None, float("-inf")
        for option, child, new_player in self.children1(board, player):
            if new_player  ==  player.name:
                _, utility = self.maximize(child, new_player, alfa, beta, depth - 1,players)

            else:
                _, utility = self.minimize(child, new_player, alfa, beta, depth - 1,players)
            if utility > max_utility:
                max_child, max_utility = option, utility
            alfa = max(alfa, max_utility)
            if max_utility >= beta:
                break
        return max_child, max_utility

    def minimize(self, board, player, alfa, beta, depth,players):
        if self.should_stop(board, player, depth):
            return None, -self.evaluate1(board, player)
        
        min_child, min_utility = None, float("inf")
        for option, child, new_player in self.children1(board, player):
            if new_player.name ==  player.name:
                _, utility = self.maximize(child, new_player, alfa, beta, depth - 1,players)
            else:
                _, utility = self.minimize(child, new_player, alfa, beta, depth - 1,players)
    
            if utility < min_utility:
                min_child, min_utility = option, utility
            beta = min(beta, min_utility)
            if min_utility <= alfa:
                break
        return min_child, min_utility

    def should_stop(self, board, player, depth):
        if time.time() - self.start_time >= self.max_time:
            raise StopIteration("¡Tiempo agotado!")
        return depth <= 0 or self.is_terminal(board, player)

    def evaluate(self, board, player):
        return board.cal_culo_de_puntos1(player)
    def evaluate1(self,board, player):
        #print(player.used_pieces)
        if len(player.used_pieces):
            return  self.combined_heuristics(player.used_pieces[-8],player,board)
        return self.evaluate(board, player)

    def combined_heuristics_for_minimax(self, player,board, heuristics=['heuristic_use_large_pieces_first']):
        pieces = player.used_pieces
        
        if pieces:
        
            print(pieces)
            total_cost = []
            
            for heuristic in heuristics:
                if heuristic == 'heuristic_expand_fast':
                    max1 = 1
                    total_cost.append((self.heuristic_expand_fast(player) + 0.1) / max1)
                elif heuristic == 'heuristic_use_large_pieces_first':
                    max3 = 5
                    total_cost.append((self.heuristic_use_large_pieces_first(pieces) + 0.1) / max3)
                elif heuristic == 'heurística_de_proximidad_a_la_esquina':
                    max4 = 10  # Asume que puede haber hasta 10 piezas cercanas a las esquinas
                    total_cost.append((self.heuristic_proximity_to_corner(pieces) + 0.1) / max4)
                elif heuristic == 'heurística_de_espacios_libres_adyacentes':
                    max5 = 1
                    total_cost.append((self.heuristic_minimize_opponent_pieces(pieces) + 0.1) / max5)
                elif heuristic == 'heuristic_minimize_opponent_pieces':
                    max5 = 5
                    total_cost.append((self.heuristic_proximity_to_corner(pieces) + 0.1) / max5)
                elif heuristic == 'heuristic_player_mobility':
                    max5 = 5
                    total_cost.append((self.heuristic_player_mobility(player,board) + 0.1) / max5)
            
            resultado = sum(total_cost)
            return resultado # Suma de valores heuristicos
        else:
                
            return board.cal_culo_de_puntos1(player)
            

        
