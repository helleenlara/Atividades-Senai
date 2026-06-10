numeros = []
soma = 0
pares = 0


for i in range(10):
    valor = int(input("Digite um número: "))
    numeros.append(valor)
    soma += valor
    if valor % 2 == 0:
        pares += 1


media = soma / 10
maior = numeros[0]
menor = numeros[0]


for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero


print("Soma =", soma)
print("Média =", media)
print("Maior =", maior)
print("Menor =", menor)
print("Quantidade de pares =", pares)