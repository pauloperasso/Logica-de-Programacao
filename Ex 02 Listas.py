# notas = list()

# while True:
#     print("[1] Adicionar uma nota para o aluno")
#     print("[2] Remover uma nota de um aluno")
#     print("[3] Exiba a média dos alunos")
#     print("[4] Exiba a lista de alunos e suas notas")
#     print("[5] Sair")

#     option = input("Escolha uma opção: ")

#     if option == "1":
#         notas.append(input("Digite o nome do aluno: "))
#         notas.append(input("Digite a nota do aluno: "))
#     elif option == "2":
#         if notas:
#             print("Lista de notas:", notas)
#             try:
#                 index = int(input("Digite o número do aluno que você quer remover a nota (1, 2, 3...): ")) - 1
#                 if 0 <= index < len(notas):
#                     notas.pop(index)
#                 else:
#                     print("Número inválido.")
#             except ValueError:
#                 print("Entrada inválida. Digite um número.")
#         else:
#             print("A lista está vazia.")
#     elif option == "3":
#         if notas:
#             print("Médias dos alunos:", medias)
#         else:
#             print("A lista está vazia.")
#     elif option == "4":
#         print("As notas dos alunos foram: ", notas)
#     elif option == "5":
#         print("Encerrando o programa...")
#         break
#     else:
#         print("Opção inválida. Tente novamente.")

alunos = {}

while True:
    print("[1] Adicionar uma nota para o aluno")
    print("[2] Remover uma nota de um aluno")
    print("[3] Exibir a média dos alunos")
    print("[4] Exibir a lista de alunos e suas notas")
    print("[5] Sair")

    option = input("Escolha uma opção: ")

    if option == "1":
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        
        if nome in alunos:
            alunos[nome].append(nota)
        else:
            alunos[nome] = [nota]
        
    elif option == "2":
        if alunos:
            nome = input("Digite o nome do aluno: ")
            if nome in alunos:
                print(f"Notas de {nome}: {alunos[nome]}")
                try:
                    index = int(input("Digite o número da nota que deseja remover (1, 2, 3...): ")) - 1
                    if 0 <= index < len(alunos[nome]):
                        alunos[nome].pop(index)
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
            else:
                print(f"O aluno {nome} não foi encontrado.")
        else:
            print("A lista está vazia.")
            
    elif option == "3":
        if alunos:
            for nome, notas in alunos.items():
                media = sum(notas) / len(notas)
                print(f"{nome}: Média = {media:.2f}")
        else:
            print("A lista está vazia.")
            
    elif option == "4":
        if alunos:
            for nome, notas in alunos.items():
                print(f"{nome}: {notas}\n")
        else:
            print("A lista está vazia.")
            
    elif option == "5":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
