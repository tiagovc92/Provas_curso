numero_bot = 9 
tentativas = 0 
limite = 3 

while tentativas < limite :
    numero_jogador = int(input("Dvinhe um número de 1 ate 10: "))
    tentativas += 1
    if numero_jogador == numero_bot:
       print(f"Parabéns você escolheu o número certo que é {numero_bot}")
       break
else:
    print("Suas chances acabaram ! ")
