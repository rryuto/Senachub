convidados = ["rafael", "rodrigo", "jefferson"]

nome = input("Digite o nome de um convidado: ")

if nome in convidados:
    print(f"O {nome} esta na lista de convidados")
else:
    print(f"O {nome} não esta na lista de convidados")