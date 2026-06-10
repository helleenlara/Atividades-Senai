numeros = []

for i in range(10):
    numeros.append(int(input("Digite um número: ")))


print("Ordem inversa:")


for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])