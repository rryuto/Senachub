nome = input("Nome do funcionário: ")
salario_atual = float(input("Salário atual: "))
tempo_de_empresa = int(input("Tempo de empresa: "))
nota_de_desempenho = float(input("Nota de desempenho: "))
novo_salario = 0
if nota_de_desempenho < 0 or nota_de_desempenho > 10:
    print("Nota invalida")
elif salario_atual <= 0:
    print("Salário inválido")
elif tempo_de_empresa < 0:
    print("Tempo inválido")
else: 
    if nota_de_desempenho >= 9 and tempo_de_empresa >= 5 and salario_atual < 5000:
        novo_salario = salario_atual*1.2
        print(f"Funcionário: {nome}")
        print(f"Classificação: Destaque")
        print(f"Novo salario: {novo_salario:.1f}")
    elif nota_de_desempenho >=7 and tempo_de_empresa >= 2:
        novo_salario = salario_atual*1.1
        print(f"Funcionário: {nome} ")
        print(f"Classificação: Bom")
        print(f"Novo salario: {novo_salario:.1f}")
    elif nota_de_desempenho >=5:
        novo_salario = salario_atual*1.05
        print(f"Funcionário: {nome} ")
        print(f"Classificação: Regular")
        print(f"Novo salario: {novo_salario:.1f}")
    elif nota_de_desempenho < 5:
        novo_salario = salario_atual
        print(f"Funcionário: {nome} ")
        print(f"Classificação: em Avaliação")
        print(f"Novo salario: {novo_salario:.1f}")
        



