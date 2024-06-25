from game.board import *
from game.piece import Player
from game.bots import *



def main1():
    game=Board(20)
    jugador1 = Player("Luis","red")#bot_greedy
    jugador2= Player("Manolo","blue")#bot_peores_decisiones
    jugador3= Player("Jose","yellow")#bot_aleatorio
    jugador4= Player("Maria","pink")#bot_greedy
    bot1=Bots()  
    bot2=Bots() 
    bot3=Bots() 
    bot4 =Bots()
    #bot4=MiniMax(game,jugador4,True)
    #game=bot4.minimax(game,depth=3,alpha=float("inf"),beta="-inf",maximizingPlayer=False)
    #print(a)
    
    #game = bot1.bot_greedy(game,jugador1)
    #game = bot1.bot_greedy(game,jugador1)
    jugada = bot1.solve(game,jugador1)
    print(jugada)
    game.place_piece(jugada[1],jugada[2],jugador1)
    print(game)
    #print(game[1])
    #print(game[2])
    #print(game[3])




    """
    game = bot1.bot_greedy(game,jugador1)
    game = bot1.bot_greedy(game,jugador1)
    game = bot1.bot_greedy(game,jugador1)
    game = bot1.bot_greedy(game,jugador1)
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
    #print(game.get_movable_pieces(jugador1))
    print(bot1.is_terminal(game,jugador1))
    a=bot1.children(game,jugador1)
    _,game=a[100]
    print(a[1]);print("\n")
    print(a[2]);print("\n")
    print(a[3]);print("\n")
    print(a[4]);print("\n")
    print(game)
    #print(a);print("\n")

    #print(bot2.is_terminal(game))
    #print(bot3.is_terminal(game))
    #print(bot4.is_terminal(game))
    #print(bot1.heuristica_for_state(game,jugador1))
    #print(bot2.heuristica_for_state(game,jugador2))
    #print(bot3.heuristica_for_state(game,jugador3))
    #print(bot4.heuristica_for_state(game,jugador4))
    #print(jugador2.puntos_piezas)
    #print(len(jugador3.puntos_piezas))
    #print(len(jugador4.puntos_piezas))
    print(game.cal_culo_de_puntos())
    """
def main():
    game=Board(20)
    jugador1 = Player("Luis","red")#bot_greedy
    jugador2= Player("Manolo","blue")#bot_peores_decisiones
    jugador3= Player("Jose","yellow")#bot_aleatorio
    jugador4= Player("Maria","pink")#bot_greedy
    bot1=Bots()  
    bot2=Bots() 
    bot3=Bots() 
    bot4 =Bots()
    while True:
        game = bot1.bot_greedy(game, jugador1)
        if bot1.is_terminal(game, jugador1):
            break
        game = bot2.maximize(game, jugador2,alfa=float("inf"),beta=float("-inf"),depth=3)
        #if bot1.is_terminal(game, jugador2):
        #    break
        game = bot3.bot_aleatorio(game[2], jugador3)
        if bot1.is_terminal(game, jugador3):
            break
        game = bot4.bot_greedy(game, jugador4)
        if bot1.is_terminal(game, jugador4):
            break

    # Final del juego, puedes imprimir los resultados o estadísticas aquí
    print("El juego ha terminado.")
    # Opcional: Mostrar el tablero final
    print(game)
    print(game.cal_culo_de_puntos())
    # Opcional: Calcular y mostrar el puntaje final de los jugadores
   # for player in [jugador1, jugador2, jugador3, jugador4]:
    #    score = game.calculate_score(player)
    #    print(f"Jugador {player.name} ({player.color}): {score} puntos")


    
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
