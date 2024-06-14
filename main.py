from game.board import *
from game.piece import *

def main():
    pass
def main1():
    game=Board(5)
    jugador = Player("Luis","yellow")
    game.place_piece(jugador.P_17,[0,0])
    game.display_board()

if __name__ == "__main__":
    #■
    #print("░")
    main1()

