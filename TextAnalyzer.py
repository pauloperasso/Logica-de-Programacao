def contar_palavras(texto):
    separar = texto.split()
    contador = len(separar)
    return contador

def contar_vogais(texto):
    minusculo = texto.lower()
    cont_vogal = texto.count("a") + texto.count("e") + texto.count("i") + texto.count("o") + texto.count ("u") + texto.count("A") + texto.count("E") + texto.count("I") + texto.count("O") + texto.count("U")
    return cont_vogal

def encontrar_ocorrencias(texto, palavra):
    encontrar = texto.count(palavra)
    return encontrar