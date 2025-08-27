import string_utils

def main():
    texto = input("Digite um texto: ")
    texto_tratado = string_utils.remover_espacos_e_converter_minusculo(texto)
    texto_verificado = string_utils.ehpalindromo(texto_tratado)
    print(texto_tratado)
    print(texto_verificado)
main()