notas = []
maior_nota = 0  
menor_nota = 10000
contador_aprovado = 0
contador_reprovado = 0

for i in range(5):
    nota = int(input("Nota: "))
    notas.append(nota)

for nota in notas:
    print(nota)


print("media:", sum(notas)/5)

for nota in notas:
    if nota >= maior_nota:
        maior_nota = nota
    if nota <= menor_nota:
        menor_nota = nota

print("Maior nota: ",maior_nota)
print("Menor nota: ",menor_nota)

for nota in notas:
    if nota > 5:
        contador_aprovado += 1
    else:
        contador_reprovado += 1

print("Alunos aprovados: ", contador_aprovado)
print("Alunos reprovados: ", contador_reprovado)
