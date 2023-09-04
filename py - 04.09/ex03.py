import os
numSet = {}
num = ''
while num != 0:
    print("Digite numeros inteiros(qnd quiser parar digite 0)")
    num = int(input())
    if num != 0:
        numSet.add(num)
    if os.path.exists('numeros.txt'):
        arquivo = open('numeros.txt','w',encoding='utf-8')
        arquivo.write(f'{numSet}')
        open.close()
    else:
        arquivo = open('numeros.txt', 'x', encoding='utf-8')
        arquivo.write(f'{numSet}')
    
