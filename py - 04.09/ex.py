# r- VALOR PADRÃO PARA ABRIR UM ARQUIVO PARA LEITURA
# a- ABRE O ARQUIVO PARA ADICIONAR UM CONTEÚDO
# w- ABRE O ARQUIVO PARA REESCREVER O CONTEUDO
# x- CRIA UM NOVO ARQUIVO E DÁ ERRO SE JÁ EXISTIR
import os
try:

    if os.path.exists('rato.txt'):
        os.remove('rato.txt')

    f = open('rato.txt','x',encoding='utf-8')
    f.close()

    f = open('rato.txt','a',encoding='utf-8')
    f.write("O rato roeu")
    f.write('a roupa do rei de roma')
    f.close()

    arquivo = open('texto.txt','a')
    arquivo.write('\nsou pequeninhinha')
    arquivo.close()
    
    arquivo = open('texto.txt','r', encoding='utf-8')
    for i in range(0,3,1):
        print(arquivo.readline())

    for i in arquivo:
        print(i)
    
    arquivo.close()

   
except FileNotFoundError:
    print("Arquivo não encontrado")


