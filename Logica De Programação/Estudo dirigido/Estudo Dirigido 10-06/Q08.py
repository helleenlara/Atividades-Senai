numeros = []


for i in range(8):
    numeros.append(int(input("Digite um número: ")))


print("Positivos:")


for numero in numeros:
    if numero > 0:
        print(numero)