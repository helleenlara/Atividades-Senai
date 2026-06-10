numeros = []
contador = 0


for i in range(10):
    valor = int(input("Digite um número: "))
    numeros.append(valor)


    if valor > 50:
        contador += 1

print("Maiores que 50 =", contador)