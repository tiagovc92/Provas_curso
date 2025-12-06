n1 = int(input("Digite o primeiro número que dirá o início: "))
n2 = int(input("Digite o segundo número que dirá o fim: "))

soma = 0

for i in range (n1, n2 + 1):
    if i % 2 == 0:
     soma + i 
    else :
     if soma == 0 :
        print(f"Não ha números pares de {n1} a {n2}")