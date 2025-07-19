# csv - comma separeted values
# arquivo separados por ;
import csv
# os - operationa system
# criar arquivos, gerenciar pastas
import os

# Biblioteca de graficos
import matplotlib.pyplot as plt


# nome do arquivo
ARQUIVO_CSV = "dados_senai.csv"

# verificar se o arquivo existe
arquivo_existe = os.path.exists(ARQUIVO_CSV)
# arquivo -> true || false

# salvar arquivo
def salvar_em_csv (nome, idade, email):
    # a -> acrescimo
    # newLine -> evitar linhas brancas
    # enconding -> codificação caracteres BR Ç, ~,''
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as arquivo:
        # escritor para reescrever o arquivo
        escritor = csv.writer(arquivo)

        # se o arquivo não existir
        if not arquivo:
            # cria uma nova linha | write -> escrever | row -> linha
            escritor.writerow(['nome', 'idade', 'email'])

        escritor.writerow([nome, idade, email])

# Queremos identificar a faixa de etaria dos usuarios do sistema
def mostrar_grafico():
    # le idades
    faixas = {
        '0-17': 0,
        '18-30':0,
        '31-45':0,
        '46-60':0,
        '60+':0
    }

    with open(ARQUIVO_CSV, mode='r', encoding='utf-8') as arquivo:
    # ler o documento
        leitor = csv.DictReader(arquivo)

        # enquanto tiver linhas, ele percorre
        for linha in leitor:
            try:
                idade = int(linha['idade']) # capturar a idade da coluna
                if idade <= 17:             # verifico a etapa
                    faixas['0-17'] += 1     # caso ela esteja, soma mais uma    
                elif idade <= 30:
                    faixas['18-30'] += 1
                elif idade <= 45:
                    faixas['31-45'] += 1
                elif idade <= 60:
                    faixas['46-60'] +=1
                else:       
                    faixas['60+'] +=1
            except ValueError:
                continue


        # primeiro chave e depois valor        
        plt.bar(faixas.keys(), faixas.values(), color='skyblue')   
        plt.title('Distribuição por Faixa Etaria')
        plt.xlabel('Faixa Etaria')
        plt.ylabel('Quantidade de pessoas') 
        # linhas do grid -> true
        # tracejado e largura
        plt.grid(True, linestyle='--', alpha=0.5)
        # ajusta o layout e ajusta os graficos internos
        plt.tight_layout()
        plt.show()


# funcao principal
def main():
    # repetir infinitamente
    while True:
        print("\n Digite os dados do usuario: ")
        nome =  input("Nome: ")
        idade = input("Idade: ")
        email = input("Email: ")

        # chamando a funcao para salvar no arquivo csv
        salvar_em_csv(nome, idade, email) 
        print("Dados salvos com sucesso!")

        continuar = input("Deseja adicionar outro? s/n")
        if continuar != 's':
            break


    mostrar_grafico()        

if __name__ == '__main__':
    main()       


# python -m pip show matplotlib
# python -m pip show pandas
