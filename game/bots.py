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

    def bot_aleatorio(self):
        state = copy.deepcopy(self.board)
        frontier = state.get_movable_pieces(self.player)
        current_state= random.choice(frontier)
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],self.player)
        state.display_board()      
        print(new_state)
        return state
       
    def bot_greedy(self):
        state = copy.deepcopy(self.board)
        frontier = self.add_heuristic_value(state.get_movable_pieces(self.player))
        current_state= max(frontier, key=lambda x: x[0])
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],self.player)
        state.display_board()      
        print(new_state)
        return state
    def bot_peores_decisiones(self):
        state = copy.deepcopy(self.board)
        frontier = self.add_heuristic_value(state.get_movable_pieces(self.player))
        current_state= min(frontier, key=lambda x: x[0])
        new_state = copy.deepcopy(current_state)
        state.place_piece(new_state[1], new_state[2],self.player)
        state.display_board()      
        print(new_state)
        return state
    
    def heuristic_expand_fast(self):
        pass

    def heuristic_block_opponents(self):
        pass

    def heuristic_use_large_pieces_first(self):
        pass

    def heurística_de_proximidad_a_la_esquina(self):
        pass

    def heurística_de_espacios_libres_adyacentes(self):
        pass
    
    def add_heuristic_value(self,get_movable_pieces):
        new_get_movable_pieces=[]
        for get_movable in get_movable_pieces:
            value = self.combined_heuristics(get_movable)
            new_get_movable_pieces.append((value,get_movable[1],get_movable[2]))
        return new_get_movable_pieces  
    def min_max_normalization(self,values):
        min_val = min(values)
        max_val = max(values)
        return [(x - min_val) / (max_val - min_val) for x in values]
    
    def combined_heuristics(self, pieces,
                                heuristics = ['heuristic_expand_fast','heuristic_block_opponents',
                                            'heuristic_use_large_pieces_first',
                                            "heurística_de_proximidad_a_la_esquina",
                                            'heurística_de_espacios_libres_adyacentes']):
        total_cost = []
        for heuristic in heuristics:
            if heuristic == 'heuristic_expand_fast':
                total_cost.append(self.heuristic_expand_fast(car, exit_row, exit_col))
            elif heuristic == 'heuristic_block_opponents':
                total_cost.append(self.heuristic_block_opponents(car, exit_row, exit_col))
            elif heuristic == 'heuristic_use_large_pieces_first':
                total_cost.append(self.heuristic_use_large_pieces_first(car, exit_row, exit_col))
            elif heuristic == 'heurística_de_proximidad_a_la_esquina':
                total_cost.append(self.heurística_de_proximidad_a_la_esquina(car, exit_row, exit_col))
            elif heuristic == 'heurística_de_espacios_libres_adyacentes':
                total_cost.append(self.heurística_de_espacios_libres_adyacentes(car, exit_row, exit_col))
        
        return self.min_max_normalization(total_cost)

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