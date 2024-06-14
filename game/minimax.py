import time
import pandas as pd
import os
import tracemalloc
class MiniMax:
    def __init__(self, board):
        self.board = board
    def metricas(ganador, puntos, tiempo_ejecucion, memoria_actual, memoria_maxima, ruta, tamaño_de_la_ruta):
        # Verificar si el archivo existe
        if os.path.exists("metricas.csv"):
            df = pd.read_csv("metricas.csv")
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