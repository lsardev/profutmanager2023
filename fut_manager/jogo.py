import jogadores
from random import randint
from time import sleep
import pandas as pd

<<<<<<< Updated upstream
print(jogadores.escalacao_titular("Palmeiras"))
=======
#print(jogadores.escalacao_titular("Palmeiras"))

>>>>>>> Stashed changes
#Começo do jogo - Mostra escalação
def jogar_jogo(time1, time2):
    hometeam = jogadores.escolher_time_titular_4_3_3(time1)
    awayteam = jogadores.escalacao_titular(time2)

    return [hometeam, awayteam]

#comecar_jogo("Palmeiras", "Flamengo")

#simular jogo
def simular_jogo(time1, time2):
    hometeam = jogadores.escalacao_titular(time1)
    awayteam = jogadores.escalacao_titular(time2)

    return [hometeam, awayteam]

#envolvimento da partida
def envolvimento_da_partida(time1, time2):
    times_na_partida = jogar_jogo(time1, time2)

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
        

<<<<<<< Updated upstream
    print("{} {} x {} {}".format(time1, gol_seu, gol_adversario, time2))      
=======
    print("{} {} x {} {}".format(time1, gol_seu, gol_adversario, time2)) 

    lista_com_time = []
    if gol_seu > gol_adversario:
        lista_com_time.append(time1)
    elif gol_adversario > gol_seu:
        lista_com_time.append(time2)
    elif gol_adversario == gol_seu:
        lista_com_time.append("Empate")
    else:
        print("Erro")
        lista_com_time.append("Erro")

    return [lista_com_time[0], gol_seu, gol_adversario]
    
>>>>>>> Stashed changes

#envolvimento da partida simulada
def envolvimento_da_partida_simulada(time1, time2):
    times_na_partida = simular_jogo(time1, time2)

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

        if num == 1:
            # variavel para definir qual jogador fez o gol do seu time
            randint_jogador_que_fez_o_gol = randint(0, 3)

            gol_seu += 1

            if randint_jogador_que_fez_o_gol == 0:
                ofensivo = times_na_partida[0][1][0]
            
            elif randint_jogador_que_fez_o_gol == 1:
                ofensivo = times_na_partida[0][1][1]

            elif randint_jogador_que_fez_o_gol == 2:
                ofensivo = times_na_partida[0][1][2]

            elif randint_jogador_que_fez_o_gol == 3:
                ofensivo = times_na_partida[0][1][3]

            print("O jogador {} fez gol".format(ofensivo))

        if num2 == 1:

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

            print("O jogador {} fez gol".format(ofensivo))

    print("{} {} x {} {}".format(time1, gol_seu, gol_adversario, time2)) 

<<<<<<< Updated upstream
=======
    if gol_seu > gol_adversario:
        time_vencedor = time1
        gols_time_vencedor = gol_seu
        gols_time_perdedor = gol_adversario

    elif gol_adversario > gol_seu:
        time_vencedor = time2
        gols_time_vencedor = gol_adversario
        gols_time_perdedor = gol_seu

    if gol_adversario == gol_seu:
        time_vencedor = "Empate"
        gols_time_vencedor = gol_adversario
        gols_time_perdedor = gol_seu

    return [time_vencedor, gols_time_vencedor, gols_time_perdedor]
>>>>>>> Stashed changes

#envolvimento_da_partida_simulada("Botafogo", "Fluminense")
#placar final

#simulando primeiro campeonato
def copa_rio_sp(time1, time2, time3, time4):

    #sorteio
    times = [time1, time2, time3, time4]

    time_sorteado_num = randint(0, 3)
    primeiro_time_sorteado = times[time_sorteado_num]
    times.remove(primeiro_time_sorteado)

    segundo_time_sorteado_num = randint(0, 2)
    segundo_time_sorteado = times[segundo_time_sorteado_num]
    times.remove(segundo_time_sorteado)

    primeiro_time = primeiro_time_sorteado
    segundo_time = segundo_time_sorteado
    terceiro_time = times[0]
    quarto_time = times[-1]

    print("Primeiro jogo: {} x {}".format(primeiro_time, segundo_time))
    print("Segundo Jogo: {} x {}".format(terceiro_time, quarto_time))

<<<<<<< Updated upstream
copa_rio_sp("Flamengo", "Palmeiras", "Botafogo", "Fluminense")
=======
    vencedor_chave_um = envolvimento_da_partida(primeiro_time, segundo_time, sua_escalacao)
    vencedor_chave_dois = envolvimento_da_partida_simulada(terceiro_time, quarto_time)

    print("-"*30)
    print("Times que passaram de fase")
    print(vencedor_chave_um)
    print(vencedor_chave_dois)
    print("-"*30)

    if vencedor_chave_um == seutime:
        envolvimento_da_partida(vencedor_chave_um, vencedor_chave_dois, sua_escalacao)
    elif vencedor_chave_dois == seutime:
        envolvimento_da_partida(vencedor_chave_dois, vencedor_chave_um, sua_escalacao)



#copa_rio_sp_exemplo("Palmeiras", "Flamengo", "Botafogo", "Sao Paulo")

#simulacao de uma minitemporada
def mini_temporada1(lista_times):
    #escalacao
    sua_escalacao = definir_time(lista_times[0])
    #campeonatos: Copa e Brasileiro

    #campeonato brasileiro
    brasileirao_dic = {lista_times[0]:[0, 0, 0, 0], lista_times[1]:[0, 0, 0, 0], lista_times[2]:[0, 0, 0, 0], lista_times[3]:[0, 0, 0, 0], 
                       lista_times[4]:[0, 0, 0, 0], lista_times[5]:[0, 0, 0, 0], lista_times[6]:[0, 0, 0, 0], lista_times[7]:[0, 0, 0, 0]}
    df_brasileirao = pd.DataFrame(brasileirao_dic)

    num_times = len(lista_times)

    #campeonato brasileiro - função da rodada
    def partida_brasileirao(time1, time2):
        partida = envolvimento_da_partida_simulada(time1, time2)

        time = partida[0]
        gols_time_vencedor = partida[1]
        gols_time_perdedor = partida[2]

        print("{} venceu a partida".format(time))

        df_brasileirao.loc[3][time1] += 1
        df_brasileirao.loc[3][time2] += 1
        
        if time == time1:
            #estatísticas do time vencedor
            df_brasileirao.loc[0][time1] += 3
            df_brasileirao.loc[1][time1] += gols_time_vencedor

            saldo_degols_vencedor = gols_time_vencedor - gols_time_perdedor
            df_brasileirao.loc[2][time1] += saldo_degols_vencedor

            #estatísticas do time perdedor
            df_brasileirao.loc[1][time2] += gols_time_perdedor

            saldo_degols_vencedor = gols_time_perdedor - gols_time_vencedor
            df_brasileirao.loc[2][time2] += saldo_degols_vencedor

        elif time == time2:
            #estatisticas do time vencedor
            df_brasileirao.loc[0][time2] += 3
            df_brasileirao.loc[1][time2] += gols_time_vencedor

            saldo_degols_vencedor = gols_time_vencedor - gols_time_perdedor
            df_brasileirao.loc[2][time2] += saldo_degols_vencedor

            #estatística do time perdedor
            df_brasileirao.loc[1][time1] += gols_time_perdedor

            saldo_degols_vencedor = gols_time_perdedor - gols_time_vencedor
            df_brasileirao.loc[2][time1] += saldo_degols_vencedor


        elif time == "Empate":
            df_brasileirao.loc[0][time1] += 1
            df_brasileirao.loc[0][time2] += 1

            df_brasileirao.loc[1][time1] += gols_time_vencedor
            df_brasileirao.loc[1][time2] += gols_time_perdedor

    def partida_brasileirao_seutime(time1, time2):
        partida = envolvimento_da_partida(time1, time2, sua_escalacao)

        time = partida[0]
        gols_time_vencedor = partida[1]
        gols_time_perdedor = partida[2]

        print("{} venceu a partida".format(time))

        df_brasileirao.loc[3][time1] += 1
        df_brasileirao.loc[3][time2] += 1
        
        if time == time1:
            #estatísticas do time vencedor
            df_brasileirao.loc[0][time1] += 3
            df_brasileirao.loc[1][time1] += gols_time_vencedor

            saldo_degols_vencedor = gols_time_vencedor - gols_time_perdedor
            df_brasileirao.loc[2][time1] += saldo_degols_vencedor

            #estatísticas do time perdedor
            df_brasileirao.loc[1][time2] += gols_time_perdedor

            saldo_degols_vencedor = gols_time_perdedor - gols_time_vencedor
            df_brasileirao.loc[2][time2] += saldo_degols_vencedor

        elif time == time2:
            #estatisticas do time vencedor
            df_brasileirao.loc[0][time2] += 3
            df_brasileirao.loc[1][time2] += gols_time_vencedor

            saldo_degols_vencedor = gols_time_vencedor - gols_time_perdedor
            df_brasileirao.loc[2][time2] += saldo_degols_vencedor

            #estatística do time perdedor
            df_brasileirao.loc[1][time1] += gols_time_perdedor

            saldo_degols_vencedor = gols_time_perdedor - gols_time_vencedor
            df_brasileirao.loc[2][time1] += saldo_degols_vencedor


        elif time == "Empate":
            df_brasileirao.loc[0][time1] += 1
            df_brasileirao.loc[0][time2] += 1

            df_brasileirao.loc[1][time1] += gols_time_vencedor
            df_brasileirao.loc[1][time2] += gols_time_perdedor

        sleep(1)

    #rodada1
    #
    partida_brasileirao_seutime(lista_times[0], lista_times[1])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[2], lista_times[3])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[4], lista_times[5])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[6], lista_times[7])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada2
    partida_brasileirao_seutime(lista_times[0], lista_times[7])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[2], lista_times[1])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[4], lista_times[3])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[6], lista_times[5])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada3
    partida_brasileirao_seutime(lista_times[0], lista_times[3])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[2], lista_times[5])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[4], lista_times[7])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[6], lista_times[1])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada4
    partida_brasileirao_seutime(lista_times[0], lista_times[5])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[2], lista_times[7])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[4], lista_times[1])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[6], lista_times[3])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada5
    partida_brasileirao_seutime(lista_times[0], lista_times[2])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[4], lista_times[6])#r
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[1], lista_times[3])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[5], lista_times[7])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada6
    partida_brasileirao_seutime(lista_times[0], lista_times[4])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[2], lista_times[6])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[1], lista_times[7])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[5], lista_times[3])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada7
    partida_brasileirao_seutime(lista_times[0], lista_times[6])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[2], lista_times[4])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[1], lista_times[5])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[7], lista_times[3])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #returno
    #rodada8
    #
    partida_brasileirao_seutime(lista_times[0], lista_times[1])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[3], lista_times[2])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[5], lista_times[4])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[7], lista_times[6])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada9
    partida_brasileirao_seutime(lista_times[0], lista_times[7])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[1], lista_times[2])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[3], lista_times[4])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[5], lista_times[6])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada10
    partida_brasileirao_seutime(lista_times[0], lista_times[3])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[5], lista_times[2])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[7], lista_times[4])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[1], lista_times[6])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada11
    partida_brasileirao_seutime(lista_times[0], lista_times[5])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[7], lista_times[2])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[1], lista_times[4])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[3], lista_times[6])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada12
    partida_brasileirao(lista_times[0], lista_times[2])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[6], lista_times[4])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[3], lista_times[1])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[7], lista_times[5])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada13
    partida_brasileirao_seutime(lista_times[0], lista_times[4])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[6], lista_times[2])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[7], lista_times[1])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[3], lista_times[5])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    #rodada14
    partida_brasileirao_seutime(lista_times[0], lista_times[6])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[4], lista_times[2])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[5], lista_times[1])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    partida_brasileirao(lista_times[3], lista_times[7])
    print(df_brasileirao.T.sort_values(by=0, ascending=False))

    sleep(2)

    





times = ["Palmeiras", "Corinthians", "Sao Paulo", "Flamengo", "Botafogo", "Fluminense", "Atletico MG", "Internacional"]

mini_temporada1(times)

>>>>>>> Stashed changes
