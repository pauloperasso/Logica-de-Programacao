'''n1=int(input("Insira o primeiro número: "))
n2=int(input("Insira o segundo número: "))
if n2 % 3 == 0:
    print(f"A soma entre {n1} e {n2} resulta em {n1 + n2}!")
else:
    print(f"Os números escolhidos foram {n1} e {n2}!")'''

'''n1=int(input("Insira o número 01: "))
n2=int(input("Insira o número 02: "))
if n1 > n2:
    print(f"O maior número é {n1}")
else:
    print(f"O maior número é {n2}")'''

'''import math

def calcular_raizes(a, b, c):
    if a == 0:
        print("Não é uma equação do 2º grau, pois 'a' não pode ser zero.")
        return
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes da equação são x1 = {x1:.2f} e x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A equação possui uma raiz real, x = {x:.2f}")
    else:
        print("Não existem raízes reais, o discriminante é negativo.")

# Leitura dos coeficientes a, b e c
try:
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    calcular_raizes(a, b, c)
except ValueError:
    print("Por favor, insira valores numéricos válidos para os coeficientes.")'''

sl=float(input("Digite o seu salário: "))
cod=str(input("Qual o seu código? [310], [456], [885]: ")) 
cinco="310"
setemeio="456"
dez="885"
if cod == "310":
    novo_salario = sl * (1 + 15/100)  
    print(f"O seu novo salário será de R${novo_salario:.3f}")
elif cod == "456":
    novo_salario = sl * (1 + 7.5/100)  
    print(f"O seu novo salário será de R${novo_salario:.3f}")
elif cod == "885":
    novo_salario = sl * (1 + 10/100)  
    print(f"O seu novo salário será de R${novo_salario:.3f}")
else:
    print("Nenhum cargo foi selecionado!")
    novo_salario = sl * (1 + 15/100) 
    print(f"Portanto, seu novo salário será de R${novo_salario:.3f}")



