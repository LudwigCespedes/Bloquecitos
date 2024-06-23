import time
import pandas as pd
import os
import tracemalloc
import copy
import random
from collections import deque
import heapq

# Clase que representa los boots y el minimax

class Bots:

    #"Acepto invitaciones para un trio"
    def __init__(self, board,player):

        self.board = board # Tablero
        self.player = player # Jugador

# BOT ALEATORIO 

    def bot_aleatorio(self,board1,player1):

        state = copy.deepcopy(board1)
        frontier = state.get_movable_pieces(player1)

        #print(frontier) 
        current_state= random.choice(frontier)
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],player1)
        #state.display_board() 

        # Nuevo estado del tablero despues del movimiento     
        return state
       
# BOT GREEDY

    def bot_greedy(self,board1,player1):
        
        state = copy.deepcopy(board1)
        frontier = self.add_heuristic_value(state.get_movable_pieces(player1))
        current_state= max(frontier, key=lambda x: x[0])
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],player1)


        # Nuevo estado del tablero despues del movimiento     
        return state
    

# BOT PEORES DECISIONES

    def bot_peores_decisiones(self,board1,player1):

        state = copy.deepcopy(board1)
        frontier = self.add_heuristic_value(state.get_movable_pieces(player1))
        current_state= min(frontier, key=lambda x: x[0])
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],player1)
        #state.display_board()

        # Nuevo estado del tablero despues del movimiento       
        return state
    
# Primera heuristica
    
    def heuristic_expand_fast(self,piece):
        pass

# Segunda heuristica

    def heuristic_block_opponents(self):
        pass

# Tercera heuristica (Piezas mas grandes primero)

    def heuristic_use_large_pieces_first(self,matrix):

        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '■':
                    count= count + 1
        return count

# Cuarta heuristica

    def heuristic_proximity_to_corner(self, matrix):
        count = 0
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        
        if rows == 0 or cols == 0:
            return count

        corners = [(0, 0), (0, cols-1), (rows-1, 0), (rows-1, cols-1)]
        proximity_range = 2  # Considera piezas dentro de 2 celdas de las esquinas

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != '■':
                    for corner in corners:
                        if abs(corner[0] - i) <= proximity_range and abs(corner[1] - j) <= proximity_range:
                            count += 1
                            break  # Solo cuenta una vez por pieza
        
        return count

# Quita heuristica

    def heurística_de_espacios_libres_adyacentes(self):
        pass

# Agregacion de valores heuristicos a las piezas moviles
    
    def add_heuristic_value(self, get_movable_pieces):
        new_get_movable_pieces = []

        for get_movable in get_movable_pieces:
            value = self.combined_heuristics(get_movable[1], heuristics=['heuristic_use_large_pieces_first', 'heurística_de_proximidad_a_la_esquina'])
            new_get_movable_pieces.append((value, get_movable[1], get_movable[2]))
        
        return new_get_movable_pieces
    
# Normalizacion de los valores heuristicos al rango de [0, 1]

    def min_max_normalization(self,values):

        min_val = min(values)
        max_val = max(values)
        
        return [(x - min_val) / (max_val - min_val) for x in values]    


# Combinacion de las heuristicas para obtener un valor heuristico combinado

    def combined_heuristics(self, pieces, heuristics=['heuristic_use_large_pieces_first']):
        total_cost = []
        
        for heuristic in heuristics:
            if heuristic == 'heuristic_expand_fast':
                max1 = 1
                total_cost.append((self.heuristic_expand_fast(pieces) + 0.1) / max1)
            elif heuristic == 'heuristic_block_opponents':
                max2 = 1
                total_cost.append((self.heuristic_block_opponents(pieces) + 0.1) / max2)
            elif heuristic == 'heuristic_use_large_pieces_first':
                max3 = 5
                total_cost.append((self.heuristic_use_large_pieces_first(pieces) + 0.1) / max3)
            elif heuristic == 'heurística_de_proximidad_a_la_esquina':
                max4 = 10  # Asume que puede haber hasta 10 piezas cercanas a las esquinas
                total_cost.append((self.heuristic_proximity_to_corner(pieces) + 0.1) / max4)
            elif heuristic == 'heurística_de_espacios_libres_adyacentes':
                max5 = 1
                total_cost.append((self.heurística_de_espacios_libres_adyacentes(pieces) + 0.1) / max5)
        
        resultado = sum(total_cost)
        return resultado

        # Suma de valores heuristicos
        return resultado


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
    
    
# LAS METRICAS

    def metricas(ganador, puntos, tiempo_ejecucion, memoria_actual, memoria_maxima, ruta, tamaño_de_la_ruta):
        

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
            df = pd.DataFrame(columns=["ganador", "puntos", "tiempo_ejecucion", "memoria_actual", "memoria_maxima", "ruta", "tamaño_de_la_ruta"])
        
        # Crear un nuevo DataFrame con los datos a agregar
        nuevo_dato = pd.DataFrame([{
            "ganador": ganador, 
            "puntos": puntos, 
            "tiempo_ejecucion": tiempo_ejecucion, 
            "memoria_actual": memoria_actual, 
            "memoria_maxima": memoria_maxima, 
            "ruta": ruta, 
            "tamaño_de_la_ruta": tamaño_de_la_ruta
        }])
        
        
        df = pd.concat([df, nuevo_dato], ignore_index=True)
        
        df.to_csv("metricas.csv", index=False)
        
        print(f"Archivo 'metricas.csv' actualizado con éxito.")

#  LAS METRICAS 
    def metricas_x_jugador():
        pass



# EL MINIMAX
class MiniMax(Bots):
    pass