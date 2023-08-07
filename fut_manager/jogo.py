import jogadores
from random import randint
from time import sleep

print(jogadores.escalacao_titular("Palmeiras"))
#Começo do jogo - Mostra escalação
def comecar_jogo(time1, time2):
    #jogadores.escolher_time_titular_4_3_3(time1)
    hometeam = jogadores.escalacao_titular(time1)
    awayteam = jogadores.escalacao_titular(time2)

    return [hometeam, awayteam]

#comecar_jogo("Palmeiras", "Flamengo")

#envolvimento da partida
def envolvimento_da_partida(time1, time2):
    times_na_partida = comecar_jogo(time1, time2)

    time1_defesa = times_na_partida[0][0][0] + times_na_partida[0][0][1] + times_na_partida[0][0][2] + times_na_partida[0][0][3] + times_na_partida[0][0][4] + times_na_partida[0][0][5] + times_na_partida[0][0][6]
    time2_defesa = times_na_partida[1][0][0] + times_na_partida[1][0][1] + times_na_partida[1][0][2] + times_na_partida[1][0][3] + times_na_partida[1][0][4] + times_na_partida[1][0][5] + times_na_partida[1][0][6]

    time1_ataque = times_na_partida[0][0][-1] + times_na_partida[0][0][-2] + times_na_partida[0][0][-3] + times_na_partida[0][0][-4]
    time2_ataque = times_na_partida[1][0][-1] + times_na_partida[1][0][-2] + times_na_partida[1][0][-3] + times_na_partida[1][0][-4]
    print(time2_ataque)

    #chance de sair gol é ataque/defesa
    chance_time1_sair_gol = time1_ataque / time2_defesa * 10
    randint_max_range_time_1 = 100/chance_time1_sair_gol

    chance_time2_sair_gol = time2_ataque / time1_defesa * 10
    randint_max_range_time2 = 100/chance_time2_sair_gol 

    gol_seu = 0
    gol_adversario = 0

    for tempo in range(90):
        num = randint(0, int(randint_max_range_time_1*3))
        num2 = randint(0, int(randint_max_range_time2*3))


        print("Minuto: {}".format(tempo))
        sleep(1)
        if num == 1:
            # variavel para definir qual jogador fez o gol do seu time
            randint_jogador_que_fez_o_gol = randint(0, 3)

            print("Gol do seu time")
            gol_seu += 1

            if randint_jogador_que_fez_o_gol == 0:
                ofensivo = times_na_partida[0][1][0]
            
            elif randint_jogador_que_fez_o_gol == 1:
                ofensivo = times_na_partida[0][1][1]

            elif randint_jogador_que_fez_o_gol == 2:
                ofensivo = times_na_partida[0][1][2]

            elif randint_jogador_que_fez_o_gol == 3:
                ofensivo = times_na_partida[0][1][3]

            print("O jogador {} fez o gol".format(ofensivo))

        if num2 == 1:
            print("Gol do seu adversario")

            #variavel para definir qual é o jogador que fez o gol do adversario
            randint_jogador_que_fez_o_gol = randint(0, 3)


            gol_adversario += 1

            if randint_jogador_que_fez_o_gol == 0:
                ofensivo = times_na_partida[1][1][0]
            
            elif randint_jogador_que_fez_o_gol == 1:
                ofensivo = times_na_partida[1][1][1]

            elif randint_jogador_que_fez_o_gol == 2:
                ofensivo = times_na_partida[1][1][2]

            elif randint_jogador_que_fez_o_gol == 3:
                ofensivo = times_na_partida[1][1][3]

            print("O jogador {} fez o gol".format(ofensivo))

        if tempo == 45:
            print("-"*30)
            print("Final do primeiro tempo")
            print("-"*30)

            sleep(2)
        

    print("{} {} x {} {}".format(time1, gol_seu, gol_adversario, time2))      



envolvimento_da_partida("Palmeiras", "Flamengo")
#placar final