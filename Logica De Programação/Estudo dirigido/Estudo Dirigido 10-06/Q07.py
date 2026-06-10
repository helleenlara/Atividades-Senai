numeros = []
impares = 0


for i in range(10):
    valor = int(input("Digite um número: "))
    numeros.append(valor)


    if valor % 2 != 0:
        impares += 1


print("Quantidade de ímpares =", impares)