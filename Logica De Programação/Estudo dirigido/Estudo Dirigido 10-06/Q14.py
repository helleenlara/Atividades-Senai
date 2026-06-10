numeros = []
pares = []
impares = []


for i in range(10):
    valor = int(input("Digite um número: "))
    numeros.append(valor)


for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


print("Pares:", pares)
print("Ímpares:", impares)
