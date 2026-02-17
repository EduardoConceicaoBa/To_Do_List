tarefas = []

while True:
    print("\nO QUE VOCE DESEJA FAZER:")
    print("1 - Adicionar Tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("4 - Sair")

    opcao = input("Escolha a sua opção: ")

    if opcao == "1":
        nova_tarefa = input("Qual tarefa voce quer adicionar: ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Não há tarefas para remover.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(i + 1, "-", tarefa)

            numero = int(input("Digite o número da tarefa que deseja remover: "))

            if 1 <= numero <= len(tarefas):
                tarefas.pop(numero - 1)
                print("Tarefa removida com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(i + 1, "-", tarefa)

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
