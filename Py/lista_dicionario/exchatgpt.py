pessoas = []

for i in range(3):
    nome = input("NOME: ")
    idade = int(input("IDADE: "))
    pessoas.append({
        "nome": nome,
        "idade": idade
    })

print(pessoas)

nome = input("Procurar um nome na lista:")

for n in pessoas:
    if n["nome"] == nome:
        print("Nome existe na lista")
        print(f"{n}")

maior = {"idade": -1}

for i in pessoas:
    if i["idade"] > maior["idade"]:
        maior = i

print(f"Maior idade é{maior}")

#media das idades
total = 0
for i in pessoas:
    total = total + i["idade"]

print(f"Média da idade é: {total/len(pessoas)}")
