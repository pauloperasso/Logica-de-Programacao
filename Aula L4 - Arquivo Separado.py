from math import sqrt, exp, log, sin  #Importando funções específicas, Boa prática de programação!
from math import * #Importando todas as funções sem usar o prefixo

comprimento = float(input("Digite um número: "))
comprimento_cm = comprimento * 100
comprimento_pol = comprimento_cm / 2.54
comprimento_pés= comprimento_pol / 12
comprimento_jardas= comprimento_pés / 3
comprimento_milhas= comprimento_jardas / 1760
print(f"O valor {comprimento} corresponde a {comprimento_cm:.1f}cm, {comprimento_pol:.2f} polegadas, etc")


valor_inicial=float(input("Digite o Investimento Inicial= "))
juros=float(input("Digite a taxa de juros estipulada = "))
periodo=int(input("Digite o período de investimento (anos): "))
calculo= valor_inicial * ( 1 + juros/100)**periodo
print(f"O valor final foi de R${calculo:.2f}")

