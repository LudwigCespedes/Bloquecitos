class Player:

# Clase que representa a el jugador en Blokus

    def __init__(self, name, color):

        self.color = color # Color del jugador
        self.name = name # Nombre del jugador
        # Diccionario de los colores
        self.colors = {
            "red": 1,   
            "blue": 2,             
            "yellow": 3,
            "pink": 4    
                        }    
        self.color_type = self.colors.get(self.color.lower(), '■') # Tipo de color del jugador
        self.pieces = self.define_pieces() # Lista de las piezas del jugador
        self.used_pieces = [] #Conjunto de piezas utilizadas por el jugador
        self.puntos_piezas = []



# Definición de las formas de las piezas 
        self.P_1 = [
            [self.color_type, self.color_type, self.color_type, self.color_type]
        ]

        self.P_2 = [
            [self.color_type, self.color_type, self.color_type, self.color_type],
            ['■', '■', self.color_type, '■']
        ]

        self.P_3 = [
            [self.color_type, '■'],
            [self.color_type, '■'],
            [self.color_type, self.color_type]
        ]

        self.P_4 = [
            [self.color_type, self.color_type],
            [self.color_type, '■'],
            [self.color_type, '■']
        ]

        self.P_5 = [
            [self.color_type, self.color_type],
            [self.color_type, self.color_type],
            [self.color_type, '■']
        ]

        self.P_6 = [
            [self.color_type, '■', '■'],
            [self.color_type, '■', '■'],
            [self.color_type, self.color_type, self.color_type]
        ]

        self.P_7 = [
            [self.color_type, self.color_type, '■'],
            ['■', self.color_type, '■'],
            ['■', self.color_type, self.color_type]
        ]

        self.P_8 = [
            ['■', self.color_type, '■'],
            [self.color_type , self.color_type , self.color_type],
            ['■', self.color_type, '■']
        ]

        self.P_9 = [
            [self.color_type,'■'],
            [self.color_type, self.color_type],
            [self.color_type, '■']
        ]

        self.P_10 = [
            [self.color_type, self.color_type],
            [self.color_type, '■'],
            [self.color_type, self.color_type]
        ]

        self.P_11 = [
            [self.color_type, '■', '■'],
            [self.color_type , self.color_type , '■'],
            ['■', self.color_type, self.color_type]
        ]

        self.P_12 = [
            [self.color_type, self.color_type, self.color_type],
            ['■', self.color_type, '■'],
            ['■', self.color_type, '■']
        ]

        self.P_13 = [
            [self.color_type, self.color_type, '■'],
            ['■', self.color_type, self.color_type],
            ['■', self.color_type, '■']
        ]

        self.P_14 = [
            [self.color_type, self.color_type, self.color_type, '■'],
            ['■', '■', self.color_type, self.color_type]
        ]

        self.P_15 = [
            [self.color_type, self.color_type, '■'],
            ['■', self.color_type, self.color_type]
        ]

        self.P_16 = [
            [self.color_type, '■'],
            [self.color_type, self.color_type]
        ]

        self.P_17 = [
            [self.color_type,self.color_type],
            [self.color_type,self.color_type]
        ]

        self.P_18 = [
            [self.color_type]
        ]

        self.P_19 = [
            [self.color_type,self.color_type,self.color_type,self.color_type,self.color_type]
        ]

        self.P_20 = [
            [self.color_type,self.color_type,self.color_type]
        ]

        self.P_21 = [
            [self.color_type,self.color_type]
        ]
    
# JUGADOR 

# Refleja una pieza horizontalmente

    def mirror_piece(self,piece):

        mirrored_piece = [row[::-1] for row in piece]
        piece.clear()  
        piece.extend(mirrored_piece)  
        return piece
    
# Transpone una pieza
   
    def transpose_piece(self,piece):

        transposed_piece = [[piece[fil][colm] for fil in range(len(piece))] for colm in range(len(piece[0]))]
        piece.clear()  
        piece.extend(transposed_piece)  
        return piece
    

# Todas las formas posibles de transposicion y espejo de una piesa

    def all_transpositions(self, piece):
        transpositions = []
        current_piece = piece

        # Pieza original
        transpositions.append(current_piece)
        
        # Transpuesta (90 grados de rotación)
        transposed_piece = [[current_piece[row][col] for row in range(len(current_piece))] for col in range(len(current_piece[0]))]
        transpositions.append(transposed_piece)
        
        # Rotación 180 grados
        rotated_180_piece = [row[::-1] for row in reversed(current_piece)]
        transpositions.append(rotated_180_piece)
        
        # Rotación 270 grados
        rotated_270_piece = [[current_piece[row][col] for row in reversed(range(len(current_piece)))] for col in range(len(current_piece[0]))]
        transpositions.append(rotated_270_piece)
        
        # Espejo
        mirrored_piece = [row[::-1] for row in current_piece]
        transpositions.append(mirrored_piece)
        
        # Transpuesta de espejo
        mirrored_transposed_piece = [[mirrored_piece[row][col] for row in range(len(mirrored_piece))] for col in range(len(mirrored_piece[0]))]
        transpositions.append(mirrored_transposed_piece)
        
        # Rotación 90 grados del espejo
        rotated_mirror_piece = [[mirrored_piece[row][col] for row in range(len(mirrored_piece))] for col in range(len(mirrored_piece[0]))]
        transpositions.append(rotated_mirror_piece)
        
        # Rotación 180 grados del espejo
        rotated_mirror_180_piece = [row[::-1] for row in reversed(mirrored_piece)]
        transpositions.append(rotated_mirror_180_piece)
        
        return transpositions

    def define_pieces(self):
        all_piece = []
        yatusabe = [
            [[self.color_type, self.color_type, self.color_type, self.color_type]],
            [[self.color_type, self.color_type, self.color_type, self.color_type], ['■', '■', self.color_type, '■']],
            [[self.color_type, '■'], [self.color_type, '■'], [self.color_type, self.color_type]],
            [[self.color_type, self.color_type], [self.color_type, '■'], [self.color_type, '■']],
            [[self.color_type, self.color_type], [self.color_type, self.color_type], [self.color_type, '■']],
            [[self.color_type, '■', '■'], [self.color_type, '■', '■'], [self.color_type, self.color_type, self.color_type]],
            [[self.color_type, self.color_type, '■'], ['■', self.color_type, '■'], ['■', self.color_type, self.color_type]],
            [['■', self.color_type, '■'], [self.color_type, self.color_type, self.color_type], ['■', self.color_type, '■']],
            [[self.color_type, '■'], [self.color_type, self.color_type], [self.color_type, '■']],
            [[self.color_type, self.color_type], [self.color_type, '■'], [self.color_type, self.color_type]],
            [[self.color_type, '■', '■'], [self.color_type, self.color_type, '■'], ['■', self.color_type, self.color_type]],
            [[self.color_type, self.color_type, self.color_type], ['■', self.color_type, '■'], ['■', self.color_type, '■']],
            [[self.color_type, self.color_type, '■'], ['■', self.color_type, self.color_type], ['■', self.color_type, '■']],
            [[self.color_type, self.color_type, self.color_type, '■'], ['■', '■', self.color_type, self.color_type]],
            [[self.color_type, self.color_type, '■'], ['■', self.color_type, self.color_type]],
            [[self.color_type, '■'], [self.color_type, self.color_type]],
            [[self.color_type, self.color_type], [self.color_type, self.color_type]],
            [[self.color_type]],
            [[self.color_type, self.color_type, self.color_type, self.color_type, self.color_type]],
            [[self.color_type, self.color_type, self.color_type]],
            [[self.color_type, self.color_type]]
        ]
        
        for i in yatusabe:
            all_piece.extend(self.all_transpositions(i))
            #self.puntos_piexas.append(self.all_transpositions(i))

        
        return all_piece
    



# Lista de las piezas del jugador
    def get_pieces(self):

        return self.pieces
    
