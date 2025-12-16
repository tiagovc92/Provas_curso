produtos = {}
total = 0

for i in range (5):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos[nome] = preco
    
valor_total = sum(produtos.values())

print(f"Os produtos cadastrados foram: ", list(produtos))

print(f"Valor total da compra: {valor_total:.2f}")


