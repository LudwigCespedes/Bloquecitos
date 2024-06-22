class Player:
    def __init__(self, name, color):
        ""
        self.color = color
        self.name = name
        self.colors = {
            "red": 1,   
            "blue": 2,
            "yellow": 3,
            "pink": 4    
                        }    
        self.color_type = self.colors.get(self.color.lower(), '■')
        self.pieces = self.define_pieces()
        self.used_pieces = set()
        """     
        if  self.color.lower() == "red":
            self.color_type = self.colors["red"]

        elif  self.color.lower() == "blue":
            self.color_type = self.colors["blue"]

        elif  self.color.lower() == "yellow":
            self.color_type = self.colors["yellow"]
            
        elif  self.color.lower() == "pink":
            self.color_type = self.colors["pink"]
        else:
            print("si")
        """




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
    
    def mirror_piece(self,piece):
        #print("Pieza transpuesta:")
        mirrored_piece = [row[::-1] for row in piece]
        
        #for row in mirrored_piece:
         #   print(row)
        piece.clear()  
        piece.extend(mirrored_piece)  
        return piece
    
    def transpose_piece(self,piece):
        #"Pieza transpuesta:"
        transposed_piece = [[piece[fil][colm] for fil in range(len(piece))] for colm in range(len(piece[0]))]
        
        #for row in transposed_piece:
         #   print(row)
        piece.clear()  
        piece.extend(transposed_piece)  
        return piece
    
    def define_pieces(self):
        all_piece = []
        yatusabe=[
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
        """
        while yatusabe:
            ya = yatusabe.pop(0)
            all_piece.append(ya)
            all_piece.append(self.mirror_piece(ya))
            all_piece.append(self.transpose_piece(ya))
            #yatusabe.remove(ya)
            print( all_piece,"s") 
            print("sdsd",self.P_1)
            break 
        """
            
        for i in yatusabe:
            all_piece.append(i)
            all_piece.append(self.mirror_piece(i))
            all_piece.append(self.transpose_piece(i))
    
        return all_piece
    
    def define_pieces1(self):
        return [
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

    def get_pieces(self):
        return self.pieces
