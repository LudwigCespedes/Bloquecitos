import time
import pandas as pd
import os
import tracemalloc
import copy
import random
from collections import deque
class Bots:
    def __init__(self, board):
        self.board = board

    def bot_aleatorio(self,board):
        initial_state = self.copy_board()
        frontier = deque([(initial_state, [])])
        visited = set()

        while frontier:
            current_state, path = frontier.popleft()

            #if current_state.check_victory(target_car_id, exit_row, exit_col):
            #    print(f"Ganaste. Ruta: {path}")
            #    return path

            current_state_str = str(current_state.board)
            if current_state_str in visited:
                continue

            visited.add(current_state_str)
            for move in current_state.get_movable_cars():
                new_state = current_state.copy_board()
                new_state.move_car(move[0], move[1], move[2])
                new_path = path + [move]
                frontier.append((new_state, new_path))

        print("No se encontró solución.")
        return None        

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
    def __init__(self, board):
        self.board = board
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