import os;

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

def excluir(nome_evento):
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    os.remove(arquivo_nome)

def editar(nome_evento):
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    dados_novos = []

    opcao = input("Qual informação que você deseja alterar: \nNome do evento \nTipo do evento \nData do evento \nLocal do evento \nOrçamento \nEscolha: ")

    with open(arquivo_nome,"r") as arquivo:
        for linha in arquivo:
            dados_novos.append(linha.strip())

    with open(arquivo_nome,"w") as arquivo:

        if opcao == "nome":
            novo_nome = input("Digite o novo nome: ")
            dados_novos[0] = novo_nome
            nome_evento_arquivo = novo_nome.replace(' ', '_')
            arquivo_nome_novo = f"{nome_evento_arquivo}.txt"
            os.remove(arquivo_nome)

            with open(arquivo_nome_novo, "w") as arquivo:
                for itens in dados_novos:    
                    arquivo.write(itens + '\n')
                 

        elif opcao == "tipo":
            novo_tipo = input("Digite o novo tipo: ")
            dados_novos[1] = novo_tipo

        elif opcao == "data":
            nova_data = input("Digite a nova data desta forma (XX/YY/ZZZZ): ")
            dados_novos[2] = nova_data
            
        elif opcao == "local":
            novo_local = input("Digite o novo local: ")
            dados_novos[3] = novo_local

        elif opcao == "orc":
            nova_orc = input("Digite o novo orçamento: ")
            dados_novos[4] = nova_orc

       
        for itens in dados_novos:    
            arquivo.write(itens + '\n')

        
    

    


