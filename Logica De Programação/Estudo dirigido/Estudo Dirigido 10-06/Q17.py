nomes = []
notas = []
soma = 0
 
quantidade = int(input("Quantos alunos? "))
 
for i in range(quantidade):
    nome = input(f"Nome do aluno {i+1}: ")
    nota = float(input(f"Nota de {nome}: "))
    nomes.append(nome)
    notas.append(nota)
    soma += nota
 
media_turma = soma / quantidade
 
maior_nota = max(notas)
menor_nota = min(notas)
posicao_maior = notas.index(maior_nota)
posicao_menor = notas.index(menor_nota)
 
print("\n===== RELATÓRIO DA TURMA =====")
print("Média da turma =", media_turma)
print("Maior nota:", nomes[posicao_maior], "-", maior_nota)
print("Menor nota:", nomes[posicao_menor], "-", menor_nota)
 
aprovados = 0
recuperacao = 0
reprovados = 0
 
print("\nAprovados (nota >= 7):")
for i in range(len(nomes)):
    if notas[i] >= 7:
        print("-", nomes[i], "-", notas[i])
        aprovados += 1
 
print("\nEm recuperação (5 <= nota < 7):")
for i in range(len(nomes)):
    if 5 <= notas[i] < 7:
        print("-", nomes[i], "-", notas[i])
        recuperacao += 1
 
print("\nReprovados (nota < 5):")
for i in range(len(nomes)):
    if notas[i] < 5:
        print("-", nomes[i], "-", notas[i])
        reprovados += 1
 
print("\nTotal aprovados:", aprovados)
print("Total em recuperação:", recuperacao)
print("Total reprovados:", reprovados)
