import random
x = random.randint(1, 11)
chute = int(input("Digite seu chute: "))
while chute != x:
    if chute == 0:
        print(f"O jogo foi encerrado! Pensei no número {x}.")
        break
    else:
        print("Tente Novamente!")
    chute=int(input("Digite seu chute ou digite 0 para sair: "))
if chute == x:
    print("Parabéns, você acertou!")
