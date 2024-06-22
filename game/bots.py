import time
import pandas as pd
import os
import tracemalloc
import copy
import random
from collections import deque
import heapq
class Bots:
    def __init__(self, board,player):
        self.board = board
        self.player = player

    def bot_aleatorio(self,board1,player1):

        state = copy.deepcopy(board1)
        frontier = state.get_movable_pieces(player1)
        #print(frontier)
        current_state= random.choice(frontier)
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],player1)
        #state.display_board()      

        return state
       
    def bot_greedy(self,board1,player1):
        state = copy.deepcopy(self.board1)
        frontier = self.add_heuristic_value(state.get_movable_pieces(self.player))
        current_state= max(frontier, key=lambda x: x[0])
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],self.player)
        #state.display_board()      
        return state
    
    def bot_peores_decisiones(self,board1,player1):

        state = copy.deepcopy(board1)
        frontier = self.add_heuristic_value(state.get_movable_pieces(player1))
        current_state= min(frontier, key=lambda x: x[0])
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],self.player)
        #state.display_board()      
        return state
    
    def heuristic_expand_fast(self,piece):
        pass
    def count_corners(matrix):
        """
        Counts the corners of a matrix where there are non-empty values.
        
        Parameters:
        - matrix: A 2D list representing the matrix.
        
        Returns:
        - count: The number of corners with non-empty values.
        """
        count = 0
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        lados_c = 4
        for i,i2 in enumerate(rows):

            for j, j2 in enumerate(cols):
                if rows == 0 or cols == 0:
                    return 0
                if matrix[i][j] != '■':
                    count =+ 4
                    if count>4 :
                        count =-4
        return count


        

    def heuristic_block_opponents(self):
        pass

    def heuristic_use_large_pieces_first(self,matrix):
        """
        Las piezas más grandes obtienen una puntuación más alta, fomentando su uso temprano en el juego cuando hay más espacio disponible.
        """
        #print(matrix,"toy")
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '■':
                    count= count + 1
        return count

    def heurística_de_proximidad_a_la_esquina(self):
        pass

    def heurística_de_espacios_libres_adyacentes(self):
        pass
    
    def add_heuristic_value(self,get_movable_pieces):
        new_get_movable_pieces=[]
        
        for get_movable in get_movable_pieces:
    
            value = self.combined_heuristics(get_movable[1],heuristics=['heuristic_use_large_pieces_first'])
            
            new_get_movable_pieces.append((value,get_movable[1],get_movable[2]))
    
        return new_get_movable_pieces  
    
    def min_max_normalization(self,values):
        min_val = min(values)
        max_val = max(values)
        return [(x - min_val) / (max_val - min_val) for x in values]
    
    def combined_heuristics(self, pieces,
                                heuristics = [
                                            'heuristic_use_large_pieces_first'
                                            ]):
        total_cost =[]
        
        for heuristic in heuristics:
            if heuristic == 'heuristic_expand_fast':
                max1 =1
                total_cost.append((self.heuristic_expand_fast(pieces)+0.1)/max1)
            elif heuristic == 'heuristic_block_opponents':
                max2 =1
                total_cost.append((self.heuristic_block_opponents(pieces)+0.1)/max2)
            elif heuristic == 'heuristic_use_large_pieces_first':
                max3 =5
                
                total_cost.append((self.heuristic_use_large_pieces_first(pieces)+0.1)/max3)
            elif heuristic == 'heurística_de_proximidad_a_la_esquina':
                max4 =1
                total_cost.append((self.heurística_de_proximidad_a_la_esquina(pieces)+0.1)/max4)
            elif heuristic == 'heurística_de_espacios_libres_adyacentes':
                max5 =1
                total_cost.append((self.heurística_de_espacios_libres_adyacentes(pieces)+0.1)/max5)
        resultado=sum(total_cost)
        #return self.min_max_normalization(total_cost)
        return resultado

    def metricas(ganador, puntos, tiempo_ejecucion, memoria_actual, memoria_maxima, ruta, tamaño_de_la_ruta):
        # Verificar si el archivo existe

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

    def metricas_x_jugador():
        pass

class MiniMax(Bots):
    pass