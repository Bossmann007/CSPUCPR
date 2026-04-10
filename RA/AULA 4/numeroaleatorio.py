import random

numero = random.randint(1, 10)
tenta = 0

while True:
    palpite = int(input("Digite um numero entre 1 e 10: "))
    tenta += 1
    if palpite < numero:
        print("O numero é maior")
    elif palpite > numero:
        print("O numero é menor")
    else:
        print(f"Parabens! Você acertou o numero {numero} em {tenta} tentativas!")
        break