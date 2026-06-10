numeros = []
pares = 0


for i in range(10):
    valor = int(input("Digite um número: "))
    numeros.append(valor)


    if valor % 2 == 0:
        pares += 1


print("Quantidade de pares =", pares)