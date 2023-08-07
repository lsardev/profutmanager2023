from random import randint

class Time:
    class Estadio:
        def __init__(self, capacidade, capacidade_da_geral, capacidade_da_arquibancada, capacidade_da_cadeira, capacidade_camarote, renda_geral, renda_arquibancada, renda_cadeira, renda_camarote, socio_torcedor):
            self.capacidade = capacidade
            self.capacidade_da_geral = capacidade_da_geral
            self.capacidade_da_arquibancada = capacidade_da_arquibancada
            self.capacidade_da_cadeira = capacidade_da_cadeira
            self.capacidade_camarote = capacidade_camarote

            self.ingresso_geral_valor = renda_geral 
            self.ingresso_arquibancada_valor = renda_arquibancada
            self.ingresso_cadeira_valor= renda_cadeira 
            self.ingresso_camarote_valor = renda_camarote  

            self.socio_torcedor = socio_torcedor 

        def publico_e_renda(self, fase_do_time):
            renda_total = int(self.capacidade_da_geral) * int(self.ingresso_geral_valor) + int(self.capacidade_da_arquibancada) * int(self.ingresso_arquibancada_valor) + int(self.capacidade_da_cadeira) * int(self.ingresso_cadeira_valor) + int(self.capacidade_camarote) * int(self.ingresso_camarote_valor)
            publico_total = int(self.capacidade)

            diferenca_renda = randint(100000, 500000)
            diferenca_publico = randint(100, 1000)
                
            #fases: Ótima, Boa, Mediana, Ruim, Péssima
            if fase_do_time.lower() == "otima":
                renda_total = renda_total - diferenca_renda
                publico_total = publico_total - diferenca_publico   

            elif fase_do_time.lower() == "boa":
                renda_total = renda_total/5*4 - diferenca_renda
                publico_total = publico_total/5*4 - diferenca_publico

            elif fase_do_time.lower() == "mediana":
                renda_total = renda_total/5*3 - diferenca_renda
                publico_total = publico_total/5*3 - diferenca_publico

            elif fase_do_time.lower() == "ruim":
                    renda_total = renda_total/5*2 - diferenca_renda
                    publico_total = publico_total/5*2 - diferenca_publico

            elif fase_do_time.lower() == "pessima":
                renda_total = renda_total/5*1 - diferenca_renda
                publico_total = publico_total/5*1 - diferenca_publico

            renda_total = int(renda_total)/100*80
            return ['{:.2f}'.format(renda_total), '{:.2f}'.format(publico_total)]


#estadios
palmeiras = Time()
EstadioAlianzParque = palmeiras.Estadio("43713", "7713", "21000", "14800", "200", "90", "150", "200", "500", "154000")

print(EstadioAlianzParque.publico_e_renda("Pessima"))

