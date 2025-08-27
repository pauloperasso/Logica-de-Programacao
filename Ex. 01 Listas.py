compras = list()

while True:
    print("[1] Adicionar um item à lista")
    print("[2] Remover um item da lista")
    print("[3] Exibir os itens da lista")
    print("[4] Limpar a lista de compras")
    print("[5] Sair")

    option = input("Escolha uma opção: ")

    if option == "1":
        compras.append(input("Digite o item que você quer adicionar: "))
    elif option == "2":
        if compras:
            print("Lista de compras:", compras)
            try:
                index = int(input("Digite o número do item que deseja remover (1, 2, 3...): ")) - 1
                if 0 <= index < len(compras):
                    compras.pop(index)
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
        else:
            print("A lista está vazia.")
    elif option == "3":
        if compras:
            print("Itens da lista:", compras)
        else:
            print("A lista está vazia.")
    elif option == "4":
        compras.clear()
        print("Lista de compras apagada.")
    elif option == "5":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
