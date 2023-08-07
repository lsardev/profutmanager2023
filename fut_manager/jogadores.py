class Elenco:
    class Jogador:
        def __init__(self, time, nome, numero, posicao, salario, valor, nacionalidade, idade, contrato_fim, finalizacao, armacao, cruzamento, marcacao, desarme, gol, lesionado, risco_de_lesao, emprestado, time_emprestimo):
            self.time = time
            self.nome = nome
            self.numero = numero
            self.posicao = posicao
            self.salario = salario
            self.valor_de_mercado = valor
            self.nacionalidade = nacionalidade
            self.idade = idade
            self.contrato_fim = contrato_fim
            self.fin = finalizacao
            self.arm = armacao
            self.cru = cruzamento
            self.mar = marcacao
            self.des = desarme
            self.gol = gol
            self.lesionado = lesionado
            self.risco_de_lesao = risco_de_lesao
            self.emprestado = emprestado
            self.time_emprestimo = time_emprestimo

            if self.posicao == "Goleiro":
                self.ovr = self.gol
            else:
                self.ovr = '{:.0f}'.format((self.fin + self.arm + self.cru + self.mar + self.des)/5)

# times
palmeiras = Elenco()
flamengo = Elenco()

#jogadores
jogadores = []

#Palmeiras

#goleiros
weverton_palmeiras = palmeiras.Jogador("Palmeiras", "Weverton", 21, "Goleiro", 650000, 15000000, "Brasileiro", 35, "31/12/2024", 21, 45, 66, 11, 11, 85, False, 3, "Null", "Null")
jogadores.append(weverton_palmeiras)

marcelolomba_palmeiras = palmeiras.Jogador("Palmeiras", "Marcelo Lomba", 42, "Goleiro", 150000, 1500000, "Brasileiro", 36, "31/12/2023", 15, 30, 9, 9, 9, 70, False, 10, "Null", "Null")
jogadores.append(marcelolomba_palmeiras)

#laterais esquerdos
vanderlan_palmeiras = palmeiras.Jogador("Palmeiras", "Vanderlan", 6, "Lateral Esquerdo", 80000, 40000000, "Brasileiro", 20, "31/12/2026", 56, 67, 79, 75, 77, 33, False, 6, "Null", "Null")
jogadores.append(vanderlan_palmeiras)

piquerez_palmeiras = palmeiras.Jogador("Palmeiras", "Piquerez", 22, "Lateral Esquerdo", 300000, 50000000, "Uruguaio", 24, "31/12/2025", 70, 74, 87, 77, 79, 23, False, 5, "Null", "Null")
jogadores.append(piquerez_palmeiras)

#laterais direitos
marcosrocha_palmeiras = palmeiras.Jogador("Palmeiras", "Marcos Rocha", 2, "Lateral Direito", 450000, 10000000, "Brasileiro", 34, "31/12/2023", 60, 75, 83, 76, 76, 22, False, 20, "Null", "Null")
jogadores.append(marcosrocha_palmeiras)

mayke_palmeiras = palmeiras.Jogador("Palmeiras", "Mayke", 12, "Lateral Direito", 250000, 10000000, "Brasileiro", 30, "31/12/2024", 60, 75, 75, 80, 80, 31, False, 5, "Null", "Null")
jogadores.append(mayke_palmeiras)

gustavogarcia_palmeiras = palmeiras.Jogador("Palmeiras", "Gustavo Garcia", 22, "Lateral Direito", 30000, 15000000, "Brasileiro", 20, "31/12/2026", 60, 69, 75, 69, 73, 17, False, 9, "Null", "Null")
jogadores.append(gustavogarcia_palmeiras)

#zagueiros - fin, arm, cru, mar, des
gustavogomez_palmeiras = palmeiras.Jogador("Palmeiras", "Gustavo Gomez", 15, "Zagueiro", 1500000, 45000000, "Paraguaio", 30, "31/12/2026", 77, 35, 85, 110, 110, 21, False, 10, "Null", "Null")
jogadores.append(gustavogomez_palmeiras)

murilo_palmeiras = palmeiras.Jogador("Palmeiras", "Murilo", 26, "Zagueiro", 500000, 45000000, "Brasileiro", 26, "31/12/2026", 65, 55, 60, 95, 105, 25, False, 7, "Null", "Null")
jogadores.append(murilo_palmeiras)

luan_palmeiras = palmeiras.Jogador("Palmeiras", "Luan Garcia", 13, "Zagueiro", 300000, 10000000, "Brasileiro", 30, "31/12/2026", 65, 55, 65, 90, 97, 12, False, 7, "Null", "Null")
jogadores.append(luan_palmeiras)

naves_palmeiras = palmeiras.Jogador("Palmeiras", "Naves", 34, "Zagueiro", 30000, 15000000, "Brasileiro", 21, "31/12/2026", 50, 50, 45, 77, 79, 12, False, 10, "Null", "Null")
jogadores.append(naves_palmeiras)

#volantes
gabrielmenino_palmeiras = palmeiras.Jogador("Palmeiras", "Gabriel Menino", 25, "Volante", 200000, 60000000, "Brasileiro", 22, "31/12/2025", 69, 74, 72, 69, 65, 15, False, 7, "Null", "Null")
jogadores.append(gabrielmenino_palmeiras)

zerafael_palmeiras = palmeiras.Jogador("Palmeiras", "Ze Rafael", 8, "Volante", 300000, 25000000, "Brasileiro", 30, "31/12/2025", 75, 75, 75, 75, 75, 21, False, 5, "Null", "Null")
jogadores.append(zerafael_palmeiras)

richardrios_palmeiras = palmeiras.Jogador("Palmeiras", "Richard Rios", 23, "Volante", 150000, 20000000, "Colombiano", 23, "31/12/2025", 80, 68, 55, 87, 85, 10, False, 5, "Null", "Null")
jogadores.append(richardrios_palmeiras)

#meias armadores
veiga_palmeiras = palmeiras.Jogador("Palmeiras", "Raphael Veiga", 23, "Meia Armador", 1000000, 80000000, "Brasileiro", 28, "31/12/2026", 99, 90, 90, 55, 55, 12, False, 7, "Null", "Null")
jogadores.append(veiga_palmeiras)

atuesta_palmeiras = palmeiras.Jogador("Palmeiras", "Eduard Atuesta", 20, "Meia Armador", 600000, 20000000, "Colombiano", 26, "31/12/2026", 70, 78, 56, 54, 51, 10, False, 6, "Null", "Null")
jogadores.append(atuesta_palmeiras)

#pontas direita - fin, arm, cru, mar, des
artur_palmeiras = palmeiras.Jogador("Palmeiras", "Artur", 14, "Ponta Direita", 750000, 60000000, "Brasileiro", 25, "31/12/2027", 88, 85, 85, 59, 59, 12, False, 5, "Null", "Null")
jogadores.append(artur_palmeiras)

#pontas esquerdas
dudu_palmeiras = palmeiras.Jogador("Palmeiras", "Dudu", 7, "Ponta Esquerda", 2100000, 45000000, "Brasileiro", 31, "31/01/2026", 87, 90, 80, 59, 59, 9, False, 10, "Null", "Null")
jogadores.append(dudu_palmeiras)

brenolopes_palmeiras = palmeiras.Jogador("Palmeiras", "Breno Lopes", 19, "Ponta Esquerda", 215000, 10000000, "Brasileiro", 27, "31/12/2026", 80, 75, 76, 60, 54, 10, False, 5, "Null", "Null")
jogadores.append(brenolopes_palmeiras)

#atacantes
rony_palmeiras = palmeiras.Jogador("Palmeiras", "Rony", 10, "Centro Avante", 1000000, 65000000, "Brasileiro", 28, "31/12/2026", 85, 80, 73, 75, 70, 12, False, 5, "Null", "Null")
jogadores.append(rony_palmeiras)


#Flamengo - fin, arm, cru, mar, des
matheuscunha_flamengo = flamengo.Jogador("Flamengo", "Matheus Cunha", 25, "Goleiro", 50000, 30000000, "Brasileiro", 22, "31/01/2026", 12, 24, 42, 23, 23, 74, False, 3, "Null", "Null")
jogadores.append(matheuscunha_flamengo)

#laterais direitos
wesley_flamengo = flamengo.Jogador("Flamengo", "Wesley", 43, "Lateral Direito", 60000, 30000000, "Brasileiro", 19, "31/12/2026", 75, 80, 80, 65, 69, 11, False, 5, "Null", "Null")
jogadores.append(wesley_flamengo)

#laterais_esquerdos
ayrtonlucas_flamengo = flamengo.Jogador("Flamengo", "Ayrton Lucas", 6, "Lateral Esquerdo", 100000, 45000000, "Brasileiro", 26, "31/12/2027", 75, 80, 85, 80, 75, 21, False, 5, "Null", "Null")
jogadores.append(ayrtonlucas_flamengo)

#zagueiros
davidluiz_flamengo = flamengo.Jogador("Flamengo", "David Luiz", 23, "Zagueiro", 1000000, 10000000, "Brasileiro", 36, "31/12/2023", 69, 78, 85, 90, 83, 50, False, 18, "Null", "Null")
jogadores.append(davidluiz_flamengo)

fabriciobruno_flamengo = flamengo.Jogador("Flamengo", "Fabricio Bruno", 15, "Zagueiro", 200000, 15000000, "Brasileiro", 27, "31/12/2025", 54, 70, 67, 88, 88, 21, False, 5, "Null", "Null")
jogadores.append(fabriciobruno_flamengo)

#volantes
allan_flamengo = flamengo.Jogador("Flamengo", "Allan", 21, "Volante", 800000, 35000000, "Brasileiro", 26, "31/12/2027", 75, 80, 74, 76, 70, 21, False, 8, "Null", "Null")
jogadores.append(allan_flamengo)

gerson_flamengo = flamengo.Jogador("Flamengo", "Gerson", 20, "Volante", 1000000, 75000000, "Brasileiro", 26, "31/12/2027", 80, 88, 77, 79, 73, 21, False, 6, "Null", "Null")
jogadores.append(gerson_flamengo)

#meia armador
arrascaeta_flamengo = flamengo.Jogador("Flamengo", "Arrascaeta", 14, "Meia Armador", 1500000, 100000000, "Uruguaio", 29, "31/12/2026", 86, 105, 94, 67, 59, 21, False, 7, "Null", "Null")
jogadores.append(arrascaeta_flamengo)

#ponta direita
evertonribeiro_flamengo = flamengo.Jogador("Flamengo", "Everton Ribeiro", 7, "Ponta Direita", 800000, 20000000, "Brasileiro", 34, "31/12/2023", 80, 86, 80, 70, 66, 15, False, 15, "Null", "Null")
jogadores.append(evertonribeiro_flamengo)

#ponta esquerda
brunohenrique_flamengo = flamengo.Jogador("Flamengo", "Bruno Henrique", 27, "Ponta Esquerda", 1000000, 20000000, "Brasileiro", 32, "31/12/2023", 88, 84, 82, 65, 60, 20, False, 12, "Null", "Null")
jogadores.append(brunohenrique_flamengo)

#centro avante
gabigol_flamengo = flamengo.Jogador("Flamengo", "Gabriel Barbosa", 10, "Centro Avante", 1500000, 100000000, "Brasileiro", 26, "31/12/2024", 110, 88, 82, 80, 56, 21, False, 7, "Null", "Null")
jogadores.append(gabigol_flamengo)

def escalacao_titular(time):
    jogadores_do_time = []

    for jogador in jogadores:
        if jogador.time == time:
            jogadores_do_time.append(jogador)

    print("-"*30)
    print("Time rival: {}".format(time))

    def buscar_jogador_pela_posicao(posicao_para_buscar):
        ovr_titular = 0

        for jogador in jogadores_do_time:
            if jogador.posicao == posicao_para_buscar:
                if int(jogador.ovr) > int(ovr_titular):
                    jogador_titular = jogador
                    ovr_titular = jogador.ovr

        jogadores_do_time.remove(jogador_titular)

        print(posicao_para_buscar + ": " + jogador_titular.nome + " "+ str(jogador_titular.ovr))
        return [jogador_titular.nome, jogador_titular.ovr, jogador_titular.des, jogador_titular.fin]

    goleiro = buscar_jogador_pela_posicao("Goleiro")
    lateral_direito = buscar_jogador_pela_posicao("Lateral Direito")
    lateral_esquerdo = buscar_jogador_pela_posicao("Lateral Esquerdo")
    primeiro_zagueiro = buscar_jogador_pela_posicao("Zagueiro")
    segundo_zagueiro = buscar_jogador_pela_posicao("Zagueiro")
    primeiro_volante = buscar_jogador_pela_posicao("Volante")
    segundo_volante = buscar_jogador_pela_posicao("Volante")
    meia_armador = buscar_jogador_pela_posicao("Meia Armador")
    ponta_direita = buscar_jogador_pela_posicao("Ponta Direita")
    ponta_esquerda = buscar_jogador_pela_posicao("Ponta Esquerda")
    centro_avante = buscar_jogador_pela_posicao("Centro Avante")
    print("-"*30)

    return [[goleiro[1], lateral_direito[2], lateral_esquerdo[2], primeiro_zagueiro[2], segundo_zagueiro[2], segundo_volante[2], primeiro_volante[2], meia_armador[-1], ponta_direita[-1], ponta_esquerda[-1], centro_avante[-1]], [meia_armador[0], ponta_esquerda[0], ponta_direita[0], centro_avante[0]]]

print(escalacao_titular("Flamengo"))

def ver_jogadores_do_time(time):
    elenco_time = []
    for jogador in jogadores:
        if jogador.time == time:
            elenco_time.append([jogador.nome, jogador.posicao, jogador.ovr, jogador.des, jogador.mar, jogador.arm, jogador.fin, jogador.gol])

    #ver os jogadores do time
    for jogador in elenco_time:
        print(jogador)

    
    return elenco_time

#ver_jogadores_do_time("Palmeiras")

def escolher_time_titular_4_3_3(time):
    jogadores_time = ver_jogadores_do_time(time)

    #para laterais, pontas, centroavante
    def retornar_escolha(posicao):
        while True:
            titular_escolhido = input("Digite o nome do jogador que você quer que seja titular: ")
            if titular_escolhido in posicao:
                print("O jogador escolhido foi: {}".format(titular_escolhido))
                break

            else:
                print("Não há esse jogador no seu time, escolha outro jogador")

        return titular_escolhido
    
    def retornar_escolha_dois_jogadores(posicao):
        while True:
            titular_escolhido1 = input("Digite o nome do primeiro jogador que você quer que seja titular: ")
            if titular_escolhido1 in posicao:
                print("O jogador escolhido foi: {}".format(titular_escolhido1))
                break
            
            else:
                print("Não há esse jogador no seu time, escolha outro jogador")

        while True:
            titular_escolhido2 = input("Digite o nome segundo jogador que você quer que seja titular: ")
            if titular_escolhido2 in posicao:
                print("O jogador escolhido foi: {}".format(titular_escolhido2))
                break

            else:
                print("Não há esse jogador no seu time, escolha outro jogador")

        return [titular_escolhido1, titular_escolhido2]


    def printar_escolha(variavel_posicao, string_posicao):
        print(string_posicao)
        print(variavel_posicao)
        jogador_escolhido = retornar_escolha(variavel_posicao)

        return jogador_escolhido
    
    def printar_escolha_dois_jogadores(variavel_posicao, string_posicao):
        print(string_posicao)
        print(variavel_posicao)
        jogadores_escolhidos = retornar_escolha_dois_jogadores(variavel_posicao)

        return jogadores_escolhidos

    goleiro = []
    for jogador in jogadores_time:
        if jogador[1] == "Goleiro":
            goleiro.append(jogador[0])

    goleiro_titular = printar_escolha(goleiro, "Goleiro")

    # pegando o ovr do goleiro para o jogo
    for jogador in jogadores_time:
        if jogador[0] == goleiro_titular:
            ovr_goleiro = jogador[-1]

    laterais_esquerdos = []
    for jogador in jogadores_time:
        if jogador[1] == "Lateral Esquerdo":
            laterais_esquerdos.append(jogador[0])
    lateral_esquerdo_titular = printar_escolha(laterais_esquerdos, "Lateral Esquerdo")

    #pegando ovr do lateral esquerdo
    for jogador in jogadores_time:
        if jogador[0] == lateral_esquerdo_titular:
            ovr_lateral_esq = jogador[3]

    laterais_direitos = []
    for jogador in jogadores_time:
        if jogador[1] == "Lateral Direito":
            laterais_direitos.append(jogador[0])
    lateral_direito_titular = printar_escolha(laterais_direitos, "Lateral Direito")

    #pegando ovr do lateral direito
    for jogador in jogadores_time:
        if jogador[0] == lateral_esquerdo_titular:
            ovr_lateral_dir = jogador[3]

    zagueiros = []
    for jogador in jogadores_time:
        if jogador[1] == "Zagueiro":
            zagueiros.append(jogador[0])
    zagueiros_titulares = printar_escolha_dois_jogadores(zagueiros, "Zagueiro")

    #pegando ovr dos zagueiros zagueiro
    for jogador in jogadores_time:
        if jogador[0] == zagueiros_titulares[0]:
            ovr_zag1 = jogador[3]

        if jogador[0] == zagueiros_titulares[1]:
            ovr_zag2 = jogador[3]

    volantes = []
    for jogador in jogadores_time:
        if jogador[1] == "Volante":
            volantes.append(jogador[0])
    volantes_titulares = printar_escolha_dois_jogadores(volantes, "Volante")

    #pegando ovr dos volantes
    for jogador in jogadores_time:
        if jogador[0] == volantes_titulares[0]:
            ovr_vol1 = jogador[3]

        if jogador[0] == volantes_titulares[1]:
            ovr_vol2 = jogador[3]

    meia_armador = []
    for jogador in jogadores_time:
        if jogador[1] == "Meia Armador":
            meia_armador.append(jogador[0])
    meia_armador_titular = printar_escolha(meia_armador, "Meia Armador")

    #pegando ovr do meia armador
    for jogador in jogadores_time:
        if jogador[0] == meia_armador_titular:
            ovr_meia_armador = jogador[6]

    ponta_esquerda = []
    for jogador in jogadores_time:
        if jogador[1] == "Ponta Esquerda":
            ponta_esquerda.append(jogador[0])
    ponta_esquerda_titular = printar_escolha(ponta_esquerda, "Ponta Esquerda")

    #pegando ovr do ponta esquerda
    for jogador in jogadores_time:
        if jogador[0] == ponta_esquerda_titular:
            ovr_ponta_esquerda = jogador[6]

    ponta_direita = []
    for jogador in jogadores_time:
        if jogador[1] == "Ponta Direita":
            ponta_direita.append(jogador[0])
    ponta_direita_titular = printar_escolha(ponta_direita, "Ponta Direita")

    #pegando ovr do ponta direita
    for jogador in jogadores_time:
        if jogador[0] == ponta_direita_titular:
            ovr_ponta_direita = jogador[6]

    centro_avante = []
    for jogador in jogadores_time:
        if jogador[1] == "Centro Avante":
            centro_avante.append(jogador[0])
    centro_avante_titular = printar_escolha(centro_avante, "Centro Avante")

    for jogador in jogadores_time:
        if jogador[0] == centro_avante_titular:
            ovr_centro_avante = jogador[6]



    lista_jogadores_titulares = ["Goleiro: {}".format(goleiro_titular[0]), "Lateral Direiro: {}".format(lateral_direito_titular), "Lateral Esquerdo: {}".format(lateral_esquerdo_titular),
                                 "Zagueiro: {}".format(zagueiros_titulares[0]), "Zagueiro: {}".format(zagueiros_titulares[1]), "Volantes: {}".format(volantes_titulares[0]), "Volantes: {}".format(volantes_titulares[1]),
                                 "Meia Armador: {}".format(meia_armador_titular), "Ponta Direita: {}".format(ponta_direita_titular), "Ponta Esquerda: {}".format(ponta_esquerda_titular), "Centro Avante: {}".format(centro_avante_titular)]
    
    print("-"*30)
    print("Seu time: {}".format(time))
    for posicao in lista_jogadores_titulares:
        print(posicao)

    return [[ovr_goleiro, ovr_zag1, ovr_zag1, ovr_lateral_dir, ovr_lateral_esq, ovr_vol1, ovr_vol2, ovr_meia_armador, ovr_ponta_direita, ovr_centro_avante, ovr_ponta_esquerda], [meia_armador_titular, ponta_direita_titular, ponta_esquerda_titular, centro_avante]]

#ver_jogadores_do_time("Palmeiras")
#escolher_time_titular_4_3_3("Palmeiras")
    

    


#escolher_time_titular("Palmeiras")


def transferencia(jogador, time_comprador_variavel, time_comprador, novo_salario, valor_pago, contrato_fim):
    nome = jogador.nome
    numero = jogador.numero
    posicao = jogador.posicao
    nacionalidade = jogador.nacionalidade
    idade = jogador.idade 
    fin = jogador.fin 
    arm = jogador.arm 
    cru = jogador.cru 
    mar = jogador.mar 
    des = jogador.des 
    gol = jogador.gol 

    jogadores.remove(jogador)

    #jogador.salario
    salario = novo_salario

    #jogador.valor_de_mercado
    valor = valor_pago

    #jogador.contrato_fim
    contrato_fim = contrato_fim

    jogador_variavel = time_comprador_variavel.Jogador(time_comprador, nome, numero, posicao, salario, valor, nacionalidade, idade, contrato_fim, fin, arm, cru, mar, des, gol)

    jogadores.append(jogador_variavel)

# simulação do piquerez vendido para o flamengo
#transferencia(piquerez, flamengo, "Flamengo", 500000, 20000000, "31/12/2027")
#ver_jogadores_do_time("Palmeiras")