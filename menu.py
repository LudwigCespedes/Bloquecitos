from game.board import Board
from game.piece import Player

class Menu:
    def _init_(self):
        self.board = Board(20)  # Tamaño del tablero de 20x20
        self.players = []
        self.available_colors = ["red", "blue", "yellow", "pink"]
        self.start_game()

    def start_game(self):
        self.choose_number_of_players()
        self.assign_colors()
        self.distribute_pieces()
        self.play_game()

    def choose_number_of_players(self):
        while True:
            try:
                num_players = int(input("Elija el número de jugadores (2 a 4): "))
                if 2 <= num_players <= 4:
                    self.num_players = num_players
                    break
                else:
                    print("Número de jugadores no válido. Debe ser entre 2 y 4.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número entre 2 y 4.")

    def assign_colors(self):
        for i in range(self.num_players):
            while True:
                print(f"Jugador {i+1}, elija un color: {self.available_colors}")
                color = input("Color: ").lower()
                if color in self.available_colors:
                    name = input(f"Jugador {i+1}, ingrese su nombre: ")
                    self.players.append(Player(name, color))
                    self.available_colors.remove(color)
                    break
                else:
                    print("Color no disponible. Por favor, elija otro color.")

    def distribute_pieces(self):
        for player in self.players:
            player.pieces = player.get_pieces()

    def play_game(self):
        player_index = 0
        while True:
            current_player = self.players[player_index]
            print(f"\nTurno de {current_player.name} ({current_player.color})")
            self.board.display_board()
            
            if self.is_first_move(current_player):
                self.first_move(current_player)
            else:
                self.next_moves(current_player)

            player_index = (player_index + 1) % self.num_players

    def is_first_move(self, player):
        return player.name not in self.board.players_pieces

    def first_move(self, player):
        while True:
            piece_index = self.choose_piece(player)
            piece = player.pieces[piece_index]
            position = self.choose_position(piece, corners_only=True)
            if self.board.place_piece(piece, position, player):
                del player.pieces[piece_index]
                break

    def next_moves(self, player):
        while True:
            piece_index = self.choose_piece(player, skip_option=True)
            if piece_index == -1:
                print(f"{player.name} ha pasado su turno.")
                break
            piece = player.pieces[piece_index]
            valid_moves = self.board.find_valid_moves(piece, player)
            if not valid_moves:
                print("No hay movimientos válidos disponibles para esta pieza. Elige otra pieza o pasa el turno.")
                continue
            print("Movimientos válidos disponibles:")
            for idx, move in enumerate(valid_moves):
                print(f"{idx + 1}: {move}")
            position_index = self.choose_move(valid_moves)
            position = valid_moves[position_index]
            if self.board.place_piece(piece, position, player):
                del player.pieces[piece_index]
                break

    def choose_piece(self, player, skip_option=False):
        while True:
            print("Piezas disponibles:")
            for index, piece in enumerate(player.pieces):
                print(f"{index + 1}:")
                for row in piece:
                    print(" ".join(str(val) for val in row))
                print()
            if skip_option:
                choice = input("Elija el número de la pieza a mover o 's' para saltar turno: ")
                if choice.lower() == 's':
                    return -1
            else:
                choice = input("Elija el número de la pieza a mover: ")
            try:
                piece_index = int(choice) - 1
                if 0 <= piece_index < len(player.pieces):
                    return piece_index
                else:
                    print("Número de pieza no válido.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número válido.")

    def choose_position(self, piece, corners_only=False):
        while True:
            if corners_only:
                print("Debes colocar la pieza en una esquina. Esquinas disponibles:")
                print("1: (0, 0)")
                print("2: (0, 19)")
                print("3: (19, 0)")
                print("4: (19, 19)")
                position = input("Elija el número de la esquina: ")
                try:
                    corner_index = int(position)
                    if corner_index == 1:
                        return (0, 0)
                    elif corner_index == 2:
                        return (0, 19)
                    elif corner_index == 3:
                        return (19, 0)
                    elif corner_index == 4:
                        return (19, 19)
                    else:
                        print("Esquina no válida.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número del 1 al 4.")
            else:
                print("Ingrese la posición donde desea colocar la pieza:")
                x = input("Fila (0-19): ")
                y = input("Columna (0-19): ")
                try:
                    x, y = int(x), int(y)
                    if 0 <= x <= 19 and 0 <= y <= 19:
                        return (x, y)
                    else:
                        print("Posición fuera de los límites.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese números válidos para la fila y la columna.")

    def choose_move(self, valid_moves):
        while True:
            choice = input("Elija el número del movimiento: ")
            try:
                move_index = int(choice) - 1
                if 0 <= move_index < len(valid_moves):
                    return move_index
                else:
                    print("Número de movimiento no válido.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número válido.")



    """
    def place_piece1(self, piece,position,color):
        x, y = position
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                if piece[i][j] != '■':
                    self.board[x + i][y + j] = str(color)
                    self.piece[color].append((x + i, y + j))
        self.print_board()

    """
        



    
    
