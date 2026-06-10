notas = []
soma = 0


for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
    soma += nota

media = soma / 4

print("Média =", media)