class Player:
    def __init__(self, name, color):
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
            [self.color_type, self.color_type],
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

    def define_pieces(self):
        return [
            [[self.color_type, self.color_type, self.color_type, self.color_type]],
            [[self.color_type, self.color_type, self.color_type, self.color_type], ['■', '■', self.color_type, '■']],
            [[self.color_type, '■'], [self.color_type, '■'], [self.color_type, self.color_type]],
            [[self.color_type, self.color_type], [self.color_type, self.color_type], [self.color_type, '■']],
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
