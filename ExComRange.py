num = int (input("Digite um número inteiro positivo: "))
if num < 2:
    print("Números menores que 2 não são primos.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} não é número primo, pois é divisível por {i}.')
        break
    else:
        print(f"{num} é um número primo!")
