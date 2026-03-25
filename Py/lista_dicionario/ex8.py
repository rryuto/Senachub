clima = []

while True:
    opcao = input("1.Registrar dia\n2.Relatório de variação\n3.Sair\n")

    if opcao == '1':
        dia = input("Dia da semana: ")
        maxima = input("Temperatura máxima: ")
        minima = input("Temperatura minima: ")

        clima.append(
            {"dia" : dia, "maxima" : maxima, "minima" : minima}
        )

    elif opcao == '2':
        print(f"Relatório de Variação")
        for i in clima:
            print(f"{i["dia"]}-feira Máxima de: {i["maxima"]} graus e Mínima de {i["minima"]} graus ")
    
    elif opcao == '3':
        print("Encerrando.")
        break