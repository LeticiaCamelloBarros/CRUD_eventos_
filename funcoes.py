def adicionar(nome_evento, tipo_evento, data_evento, local_evento, orcamento):
    dados = [nome_evento, tipo_evento, data_evento, local_evento, orcamento]
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
        for dado in dados:
            arquivo.write(dado + "\n")

def visualizar(nome_evento):
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())
def retornando_data_str_E_in_var():
    # essa função retornar a data de hoje (na ordem certa e sem o tempo exato que a data foi requerida ) e o dia 
    # o mes e o ano armazenado como inteiros dentro de variáveis 
    # teste essa função usando a biblioteca datetime e pedindo para printar 
    #dia_hj , mes_hj , ano_hj
    date_today_gr = (datetime.now())
    # vai sair no formato gringo 2025-11-06
    # precisa-se transformar no formato brasileiro em formato brasileiro 06-11-2025
    date_today_gr = str(date_today_gr)
    # por isso vai ser feito um macete para transformar o formato gringo em br
    # 1.pegando o date today e fazendo dele uma lista para
    # separarmos cada parte da data pelo separador '-'
    date_today_list = date_today_gr.split("-")

    # obs : o último item da lista , correspondente ao dia , vem tambem com o
    # os segundos , horas e minutos que essa data foi requerida , por isso vamos ter que
    # capturar só os dois primeiros caracteres do último item da lista e colocalos
    # no lugar da string com o tempo que a pessoa
    #  requeriu essa data (tipo: "06 23:06:56.012503")
    datetoday_Br = ""
    #  =============isolando só o dia
    item_dois_lista = list(date_today_list[2])
    item_dois_lista = item_dois_lista[0:2]
    item_dois_lista = "".join(item_dois_lista)
    date_today_list[2] = item_dois_lista
    # a seguir vai ser usado join , por que o date_today_list[0:2] , sem ele ,
    # iria ser guardado na forma de lista
    date_today_list[2] = "".join(date_today_list[2])
    # ====================
    datetoday_Br += date_today_list[2]
    dia_hj = int(date_today_list[2])
    # colocando a parte dia do mês
    datetoday_Br += "-"
    datetoday_Br += date_today_list[1]
    mes_hj = int(date_today_list[1])
    # colocando a parte do mês do ano
    datetoday_Br += "-"
    # colocando a parte do ano
    datetoday_Br += date_today_list[0]
    ano_hj = int(date_today_list[0])
    return datetoday_Br, dia_hj, mes_hj, ano_hj


date_hj, dia_hj, mes_hj, ano_hj = retornando_data_str_E_in_var()
