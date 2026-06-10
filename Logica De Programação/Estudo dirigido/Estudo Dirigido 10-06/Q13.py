numeros = []


for i in range(8):
    numeros.append(int(input("Digite um número: ")))


maior = numeros[0]
posicao = 0


for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        posicao = i


print("Maior valor =", maior)
print("Posição =", posicao)
