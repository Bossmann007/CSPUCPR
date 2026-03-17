nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))
nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

if len(nome1) > len(nome2):
    print("A pessoa com o nome mais longo é", nome1)

if len(nome2) > len(nome1):
    print("A pessoa com o nome mais longo é", nome2)

if len(nome1) > len(nome2):
    print("As pessoas têm nomes de comprimento igual.")

if idade1 > idade2:
    print("A pessoa mais velha é", nome1)

if idade2 > idade1:
    print("A pessoa mais velha é", nome2)

if idade1 == idade2:
    print("As pessoas têm a mesma idade.")
