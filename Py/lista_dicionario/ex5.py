funcionarios = [
    {"nome": "rafael", "salario": 2000},
    {"nome": "rodrigo", "salario": 4900},
    {"nome": "hugo", "salario": 5001},
    {"nome": "lorraine", "salario": 8000},
]

for i in funcionarios:
    if i["salario"] > 5000:
        print(f"{i["nome"]} recebe mais de R$5000,00")