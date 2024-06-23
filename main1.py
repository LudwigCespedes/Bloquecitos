from game.board import *
from game.piece import Player
from game.bots import *


def main():
    pass
def main1():
    game=Board(20)
    jugador1 = Player("Luis","yellow")
    jugador2= Player("Manolo","red")
    jugador3= Player("Jose","pink")
    jugador4= Player("Maria","blue")
    bot1=Bots(game,jugador1)  
    bot2=Bots(game,jugador2) 
    bot3=Bots(game,jugador3) 
    bot4=Bots(game,jugador4) 

    game = bot1.bot_greedy(game,jugador1) 
    game = bot2.bot_peores_decisiones(game,jugador2) 
    game = bot3.bot_aleatorio(game,jugador3) 
    game = bot4.bot_greedy(game,jugador4) 
    game = bot1.bot_greedy(game,jugador1) 
    game = bot2.bot_peores_decisiones(game,jugador2) 
    game = bot3.bot_aleatorio(game,jugador3) 
    game = bot4.bot_greedy(game,jugador4) 
    game = bot1.bot_greedy(game,jugador1) 
    game = bot2.bot_peores_decisiones(game,jugador2) 
    game = bot3.bot_aleatorio(game,jugador3) 
    game = bot4.bot_greedy(game,jugador4) 
    game = bot1.bot_greedy(game,jugador1) 
    game = bot2.bot_peores_decisiones(game,jugador2) 
    game = bot3.bot_aleatorio(game,jugador3) 
    game = bot4.bot_greedy(game,jugador4) 
    game = bot1.bot_greedy(game,jugador1) 
    game = bot2.bot_peores_decisiones(game,jugador2) 
    game = bot3.bot_aleatorio(game,jugador3) 
    game = bot4.bot_greedy(game,jugador4) 
    game = bot1.bot_greedy(game,jugador1) 
    game = bot2.bot_peores_decisiones(game,jugador2) 
    game = bot3.bot_aleatorio(game,jugador3) 
    game = bot4.bot_greedy(game,jugador4) 
    game = bot1.bot_greedy(game,jugador1) 
    game = bot2.bot_peores_decisiones(game,jugador2) 
    game = bot3.bot_aleatorio(game,jugador3) 
    game = bot4.bot_greedy(game,jugador4) 
    game = bot1.bot_greedy(game,jugador1) 
    game = bot2.bot_peores_decisiones(game,jugador2) 
    game = bot3.bot_aleatorio(game,jugador3) 
    game = bot4.bot_greedy(game,jugador4) 
    game = bot1.bot_greedy(game,jugador1) 
    game = bot2.bot_peores_decisiones(game,jugador2) 
    game = bot3.bot_aleatorio(game,jugador3) 
    game = bot4.bot_greedy(game,jugador4) 
    game = bot1.bot_greedy(game,jugador1) 
    game = bot2.bot_peores_decisiones(game,jugador2) 
    game = bot3.bot_aleatorio(game,jugador3) 
    game = bot4.bot_greedy(game,jugador4) 

    print(game)
    #print(jugador1.used_pieces)
    print(len(jugador1.puntos_piezas))
    print(jugador2.puntos_piezas)
    print(len(jugador3.puntos_piezas))
    print(len(jugador4.puntos_piezas))
    print(game.cal_culo_de_puntos())

if __name__ == "__main__":
    #■
    #print("░")
    #game = Menu()
    main1()
    """
    game=Board(20)
    jugador = Player("Luis","yellow")

    bot1=jugador.get_pieces()
    print(bot1)

 
    
    game=Board(20)
    jugador = Player("Luis","yellow")

    for i in jugador.get_pieces():
        bot1=Bots(game,jugador).heuristic_use_large_pieces_first(i)
        print(bot1)
    """
