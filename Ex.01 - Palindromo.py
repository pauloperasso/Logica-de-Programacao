palindromo = []

def palindromo(palavra):
#Palavra: Arara
    for i in range (len(palavra)//2):
        if palavra[i] != palavra[len(palavra) -1 - i]:
            return print("É um palíndromo")
        else:
            return print("Não é um palíndromo")
    return True

def main():
    x = input("Digite uma palavra para verificação de palíndromo: ")
main()

        

    