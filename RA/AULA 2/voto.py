#Algoritmo para decidir se a pessoa pode votar

ano=int(input("Digite seu ano de nascimento:"))
idade=2026-ano
print(f"Voce tem {idade} anos.")
if idade >=18:
    print("Voce pode votar")
else:
    falta=16-idade
    print("Voce pode votar")
print("Obrigado por usar o sistema VoteCheck :)")

