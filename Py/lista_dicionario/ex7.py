ranking = []

while True:
    print("1.Registrar Recorde")
    print("2.Ver Lider")
    print("3.Visualizar todos")
    print("4.Sair")
    opcao = int(input())

    if opcao == 1:
        nickname = input("Nickname: ")
        pontuacao = int(input("Pontuação: "))
        
        ranking.append({
            "nickname" : nickname,
            "pontuacao" : pontuacao
        })

    elif opcao == 2:
        maior = 0
        i_maior = 0
        for i, valor in enumerate(ranking):
            if valor["pontuacao"] > maior:
                maior = valor["pontuacao"]
                i_maior = i
        print(f"A maior pontuação é de {ranking[i_maior]["nickname"]} com {ranking[i_maior]["pontuacao"]} pontos")        
    
    elif opcao == 3:
        for i in ranking:
            print(f"{i["nickname"]} - {i["pontuacao"]}")
   
    elif opcao == 4:    
        print(f"GG!")
        break