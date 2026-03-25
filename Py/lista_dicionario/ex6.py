lista = []


while True:
    print("\n1. Adicionar tarefa")
    print("2. Visualizar lista")
    print("3. Concluir tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Nome da tarefa: ").strip()
        descricao = input("Descricao da tarefa: ").strip()

        lista.append(
            {
                "tarefa": nome,
                "descricao": descricao,
                "status": "Pendente",
            }
        )
        print("Tarefa adicionada com sucesso.")

    elif opcao == "2":
        if not lista:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de tarefas:")
            for item in lista:
                print(
                    f"Nome: {item['tarefa']} | "
                    f"Descricao: {item['descricao']} | "
                    f"Status: {item['status']}"
                )

    elif opcao == "3":
        nome_tarefa = input("Digite o nome da tarefa que deseja concluir: ").strip()
        tarefa_encontrada = False

        for item in lista:
            if item["tarefa"].lower() == nome_tarefa.lower():
                item["status"] = "Concluido"
                tarefa_encontrada = True
                print(f"Tarefa '{item['tarefa']}' concluida com sucesso.")
                break

        if not tarefa_encontrada:
            print("Tarefa nao encontrada.")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opcao invalida. Tente novamente.")
