numeros = []

for i in range(5):
    numeros.append(int(input("Digite um número: ")))


procurado = int(input("Número para procurar: "))


if procurado in numeros:
    print("Número encontrado!")
else:
    print("Número não encontrado!")
