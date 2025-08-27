def remover_espacos_e_converter_minusculo(texto):
    texto = texto.lower()
    texto = texto.strip()
    return texto 

def ehpalindromo(texto_tratado):
    for i in range(len(texto_tratado)//2):
        if texto_tratado[i] != texto_tratado[len(texto_tratado)-1-i]:
            return (f"A frase {texto_tratado} NÃO é um palíndromo")
        else: 
            return (f"A frase {texto_tratado} É um palíndromo")