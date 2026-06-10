numeros = []

for i in range(10):
    numeros.append(int(input("Digite um número: ")))

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("Maior =", maior)
