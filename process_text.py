import TextAnalyzer

def main():
    texto = input("Digite uma frase: ")
    opcao = input("Deseja digitar uma palavra: [S]/[N]: ")
    if opcao == "S":
        palavra = input("Digite uma palavra: ")
        print(f"A palavra {palavra} aparece {TextAnalyzer.encontrar_ocorrencias(texto, palavra)} vezes dentro da frase {texto}")
    print(f"A frase inserida tem {TextAnalyzer.contar_palavras(texto)} palavras! ")
    print(f"A frase inserida tem {TextAnalyzer.contar_vogais(texto)} vogais! ")
main()