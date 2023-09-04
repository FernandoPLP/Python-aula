import os

print("Escreva um novo ditado")
ditado = input()

if os.path.exists('ditado.txt'):
    arquivo = open('ditado.txt','a',encoding='utf-8')
    arquivo.write(f"{ditado}")
    arquivo.close()
