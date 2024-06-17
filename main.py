from game.board import *
from game.piece import Player
from menu import Menu

def main():
    game = Menu()
    return game
def main1():
    game=Board(20)
    jugador = Player("Luis","yellow")
    jugador1= Player("Manolo","red")
    game.place_piece(jugador.P_17,[0,0],jugador)
    game.place_piece(jugador1.P_21,[0,18],jugador1)
    game.place_piece(jugador.P_10,[2,2],jugador)
    game.place_piece(jugador.P_21,[1,4],jugador)
    game.display_board()
    print(game.get_movable_pieces(jugador))
    #print(game.players_pieces)
    #print(game.calculate_scores())

if __name__ == "__main__":
    #■
    #print("░")
    game = Menu()
    #main()

