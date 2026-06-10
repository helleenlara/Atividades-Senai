numeros = []

for i in range(10):
    numeros.append(int(input("Digite um número: ")))

menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

print("Menor =", menor)
