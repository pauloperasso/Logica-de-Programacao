funcionario ={
    "nome": "Marina",
    "cargo": "Analista de Dados",
    "idade": 27,
    "ativo": True
}
print(funcionario)

print("--------------------------------------------------------------\n")

print(funcionario["nome"])
print(funcionario["cargo"])

print("--------------------------------------------------------------\n")

if "email" in funcionario:
    print(funcionario["email"])
print(funcionario.get("email", "Email não encontrado"))

print("--------------------------------------------------------------\n")


funcionario["cargo"] = "Cientista de Dados"
print(funcionario["cargo"])

funcionario["salario"] = 8500
print(funcionario["salario"])

funcionario["email"] = "Marina@empresa.com"
print(funcionario["email"])

print("--------------------------------------------------------------\n")

valor_removido = funcionario.pop("ativo")
print("Valor removido:", valor_removido)
print("Após remoção:", funcionario)

print("--------------------------------------------------------------\n")

for chave in funcionario:
    print(chave, funcionario[chave])

