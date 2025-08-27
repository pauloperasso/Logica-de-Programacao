#MULTIPLICAÇÃO USANDO DEF

# a = int(input("Digite o valor de A: "))
# b = int(input("Digite o valor de B: "))

# def mult(a,b):
#     return a*b

# print(f"A multiplicação de A x B é: {mult(a,b)}")


#SOLUÇÃO NÚMERO 01 USANDO BIN NATIVO DO PYTHON

# def binario(N):
#     return bin(N)

# N = int(input("Digite um número para transformar em binário: "))
# print(binario(N))

def binario(N):
    if N < 0:
        return "Digite um número inteiro positivo."

    if N == 0:
        return "0"

    resultado = ""
    while N > 0:
        resultado = str(N % 16) + resultado
        N = N // 16

    return resultado

def main():
    N = int(input("Digite um número para transformar em binário: "))
    print(binario(N))
main()
# N = int(input("Digite um número para transformar em binário: "))
# print(binario(N))


# def somamultdiv(a,b,c,d):
#     return ((a + b) * c) / d

# a = int(input("Digite o valor de A: "))
# b = int(input("Digite o valor de B: "))
# c = int(input("Digite o valor de C: "))
# d = int(input("Digite o valor de D: "))
# print(f"O valor final corresponde a: {somamultdiv(a,b,c,d):.0f}")

# def calculoy(x):
#     y = 2*x + 3
#     return y

# y1 = calculoy(21)
# y2 = calculoy(98)
# y3 = calculoy(54)
# print(f"O resultado de Y1 é {y1}")
# print(f"O resultado de Y2 é {y2}")
# print(f"O resultado de Y3 é {y3}")

# import math

# def delta(a,b,c):
#     d = (b**2) - (4*a*c)
#     return d

# def raizes(a,b,c):
#     d = delta(a,b,c)
#     if (d < 0):
#         return None, None
#     else:
#         r1 = (-b + (math.sqrt(d)))/2*a
#         r2 = (-b - (math.sqrt(d)))/2*a
#         return r1, r2
    
# a = int(input("Digite o coeficiente A: "))
# b = int(input("Digite o coeficiente B: "))
# c = int(input("Digite o coeficiente C: "))
# r1, r2 = raizes(a,b,c)
# if r1 != None:
#     print("Raízes:")
#     print(f"R1: {r1:.2f}\nR2: {r2:.2f}")
# else: 
#     print("Não existem raízes reais para esse problema.")