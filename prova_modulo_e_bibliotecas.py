import random 

def lanca_dados():
    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)
    return dado_1 + dado_2

print(lanca_dados())

