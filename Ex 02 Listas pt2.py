from random import randint
#Pede ao usuário o tamanho da lista - caso for maior que o 0,50 não encontra o item
tamanho_lista = int(input("Digite o tamanho da lista: "))
lista = [] #Gera uma lista com o tamanho_lista inputado
for i in range(tamanho_lista):
    lista.append(randint(0, 50)) #Adiciona os 50 números aleatórios na lista criada

procurar = int(input("Digite um número entre 0 e 50 a ser procurado na lista: ")) #Gera o índice de procura em meio a lista

for posicao, numero in enumerate(lista): #Posição é a primeira variável, numero é a segunda
    #Enumerate serve para achar o indice do (número) dentro dessa lista
    if numero == procurar: 
        print(f"O número {procurar} foi encontrado na lista na posição {posicao + 1}") #Posição +1 pois sempre começa do 0, então adiciona 1 pra mostrar a posição real dele
        break
else:
    print(f"O número {procurar} não foi encontrado na lista.")
