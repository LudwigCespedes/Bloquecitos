from game.board import *
from game.piece import Player
from game.bots import *


def main():
    pass
def main1():
    game=Board(20)
    jugador = Player("Luis","yellow")
    jugador1= Player("Manolo","red")
    bot1=Bots(game,jugador1)
    bot=Bots(game,jugador)  
    #game.place_piece(jugador.P_17,[0,0],jugador)
    game=bot1.bot_peores_decisiones(game,jugador1)
    #game.place_piece(jugador.P_18,[2,2],jugador)
    game=bot.bot_peores_decisiones(game,jugador)
    game=bot1.bot_peores_decisiones(game,jugador1)
    #game.place_piece(jugador.P_18,[2,2],jugador)
    game=bot.bot_peores_decisiones(game,jugador)
    game=bot1.bot_peores_decisiones(game,jugador1)
    #game.place_piece(jugador.P_18,[2,2],jugador)
    game=bot.bot_peores_decisiones(game,jugador)
    print(game.players_pieces)
    #game=bot1.bot_peores_decisiones(game,jugador1)
    #game.place_piece(jugador.P_18,[2,2],jugador)
    #game=bot.bot_peores_decisiones(game,jugador)
    #game=bot1.bot_peores_decisiones(game,jugador1)
    #game.place_piece(jugador.P_18,[2,2],jugador)
    #game=bot.bot_peores_decisiones(game,jugador)
    #game=bot1.bot_peores_decisiones(game,jugador1)
    #game.place_piece(jugador.P_18,[2,2],jugador)
    #game=bot.bot_peores_decisiones(game,jugador)
    #game=bot1.bot_peores_decisiones(game,jugador1)
    #game.place_piece(jugador.P_18,[2,2],jugador)
    #game=bot.bot_peores_decisiones(game,jugador)

    #game=Bots(game,jugador1).bot_aleatorio()
    #game=Bots(game,jugador1).bot_aleatorio()
    #game=Bots(game,jugador1).bot_aleatorio()
    game.display_board()
    #game.place_piece(jugador1.P_21,[0,18],jugador1)
    #game.place_piece(jugador.P_10,[2,2],jugador)
    #game.place_piece(jugador.P_21,[1,4],jugador)
    #print(game)
    #print(game.get_movable_pieces(jugador))
    #print(game.players_pieces)
    #print(game.calculate_scores())

if __name__ == "__main__":
    #■
    #print("░")
    #game = Menu()
    main1()
    """
    game=Board(20)
    jugador = Player("Luis","yellow")

    for i in jugador.get_pieces():
        bot1=Bots(game,jugador).heuristic_use_large_pieces_first(i)
        print(bot1)
    """
