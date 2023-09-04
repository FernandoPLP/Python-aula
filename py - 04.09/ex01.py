import os
try:
    print("Escreva um ditado")
    ditado = input()

    if os.path.exists('ditado.txt'):
        os.remove('ditado.txt')
    
    arquivo = open('ditado.txt','x',encoding='utf-8')
    arquivo.write(f"{ditado}")
    arquivo.close()
    
   
except FileNotFoundError:
    print("Arquivo não encontrado")