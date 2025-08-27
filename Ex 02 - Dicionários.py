carrinho = [{"nome": "Produto 1", "quantidade": 10, "preço": 30.5}, 
            {"nome": "Produto 2", "quantidade": 5, "preço": 15.5}, 
            {"nome": "Produto 3", "quantidade": 2, "preço": 30.5}]
print(carrinho)

print("--------------------------------------------------------------\n")

#Calculando o total de cada item no carrinho
print("Total de cada item no carrinho:")
for item in carrinho:
    total_item = item['quantidade'] * item['preço']
    print(f"{item['nome']} - Total: R${total_item:.2f}")

print("--------------------------------------------------------------\n")

# Adicionando um novo produto ao carrinho
carrinho.append({"nome": "Produto 4", "quantidade": 1, "preço": 0.90})
print(carrinho)

print("--------------------------------------------------------------\n")

#Atualizando produto 03 para quantidade 3
carrinho[2]["quantidade"] = 3
print(carrinho)

print("--------------------------------------------------------------\n")

#Removendo o item 2 do carrinho
carrinho.pop(1)
print(carrinho)

print("--------------------------------------------------------------\n")

#Calculando o total da compra
print("Total da compra:")
total_compra = 0
for item in carrinho:
    total_item = item['quantidade'] * item['preço']
    total_compra += total_item
print(f"R${total_compra:.2f}")
print("--------------------------------------------------------------\n")
