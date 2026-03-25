caixa = 0

while True:
    soma = int(input("Adicionar ao caixa: "))
    if soma == 0:
        print(f"Total caixa: {caixa}")
        break
    caixa += soma


