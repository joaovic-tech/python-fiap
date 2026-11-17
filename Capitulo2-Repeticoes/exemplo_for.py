fim = int(input("Digite um numero para determinar o fim: "))

comeco = 1
pulos = 1

for numero in range(comeco, fim, pulos):
    print("	" + str(numero))