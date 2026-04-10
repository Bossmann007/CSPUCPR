import random
#Jogo de Sobrevivência na Ilha:TDE1
#Integrantes: Enzo Bossmann, Gabriel Henrique , Diego Feltrinn.
#Fluxograma: https://excalidraw.com/#json=I5KGBSd-NgBtuzmphhTki,dGmqNwdPLMMBWw0nT3vP9A
#Introdução
print("Bem-vindo ao jogo de sobrevivência!")
print("Você está preso em uma ilha deserta após um naufrágio.")
print("Para sobreviver, precisará tomar decisões certas. Escolhas erradas podem levar ao fracasso, enquanto boas escolhas aumentam suas chances de ser resgatado.")

#Objetivo
print("Objetivo: Tomar decisões para sobreviver e ser resgatado com o maior nível de energia possível.")

#Inicio
energia = 100
print(f"Sua energia inicial é: {energia}")

#Cenário 1
print("Cenário 1 – O Despertar na Ilha")
print("Você acorda em uma ilha deserta após um naufrágio. O sol quente bate em sua pele, e o som das ondas quebra o silêncio.")
print("Sua última lembrança é do barco afundando durante uma tempestade. Agora, você precisa tomar decisões para garantir sua sobrevivência.")

#Escolha 1
print("Escolha:")
print("1. Explorar a floresta em busca de recursos.")
print("2. Caminhar na praia e procurar sinais de vida.")

escolha1 = int(input("Digite o número da sua escolha: "))

while escolha1 != 1 and escolha1 != 2:
    print("Opção inválida! Por favor, escolha 1 ou 2.")
    escolha1 = int(input("Digite o número da sua escolha: "))

#perda energia1
perda1 = random.randint(20, 40)
energia = energia - perda1
print(f"Você perdeu {perda1} de energia. Energia restante: {energia}")

#Explorar a floresta
if escolha1 == 1:
    print("Você decide explorar a floresta em busca de recursos.")
    print("Você entra na floresta e logo encontra um pequeno rio de água cristalina. A sombra das árvores oferece um alívio do calor intenso.")
    print("Escolha:")
    print("1. Beber água do rio.")
    print("2. Procurar uma outra fonte de água.")

    escolha1a = int(input("Digite o número da sua escolha: "))

    while escolha1a != 1 and escolha1a != 2:
       print("Opção inválida! Por favor, escolha 1 ou 2.")
       escolha1a = int(input("Digite o número da sua escolha: "))

    if escolha1a == 1:
       print("Humm, voce começou a passar mal, o que deseja fazer? ")
       print("1. Beber mais água do rio.")
       print("2. Procurar uma outra fonte de água.")

       escolha1b = int(input("Digite o número da sua escolha: "))
       while escolha1b != 1 and escolha1b != 2:
         print("Opção inválida! Por favor, escolha 1 ou 2.")
         escolha1b = int(input("Digite o número da sua escolha: "))
        
       if escolha1b == 1:
         print("A água pode estar contaminada. Você começa a se sentir mal.")
         perda2 = random.randint(15, 35)
         energia = energia - perda2
         print(f"Você perdeu {perda2} de energia. Energia restante: {energia}")
       elif escolha1b == 2:
         print("Você encontra um coqueiro e consegue beber água de coco.")
         ganho1 = random.randint(5, 15)
         energia = energia + ganho1
         print(f"Você ganhou {ganho1} de energia. Energia atual: {energia}")
    
    elif escolha1a == 2:
         print("Você encontra um coqueiro e consegue beber água de coco.")
         ganho1 = random.randint(5, 15)
         energia = energia + ganho1
         print(f"Você ganhou {ganho1} de energia. Energia atual: {energia}")
#Caminhar na praia
elif escolha1 == 2:
    print("Você decide caminhar na praia sentindo o calor do sol e a areia quente sob seus pés. Você também começa a sentir fome e cansaço.")
    print("Escolha:")
    print("1. Caçar ou pescar")
    print("2. Procurar frutas")

    escolha2a = int(input("Digite o número da sua escolha: "))
    while escolha2a != 1 and escolha2a != 2:
       print("Opção inválida! Por favor, escolha 1 ou 2.")
       escolha2a = int(input("Digite o número da sua escolha: "))
    if escolha2a == 1:
       print("Você decide caçar ou pescar para conseguir comida.")
       print("Você não consegue coletar nada de proteína.")
       perda3 = random.randint(15, 35)
       energia = energia - perda3
       print(f"Você perdeu {perda3} de energia. Energia restante: {energia}")
    elif escolha2a == 2:
        print("Você decide procurar frutas na praia.")
        print("Você encontra frutas.")
        ganho2 = random.randint(10, 25)
        energia = energia + ganho2
        print(f"Você ganhou {ganho2} de energia. Energia atual: {energia}")

#Final
print("A Noite Chega!")
print("O sol começa a se pôr, e a temperatura cai rapidamente. O vento aumenta, e você sabe que precisa se preparar para a noite.")
print("Após algum tempo, você encontra destroços do barco, incluindo madeira, cordas e pedaços de tecido.")
print("Escolha:")
print("1.Construir um abrigo.")
print("2.Acender uma fogueira.")

escolha3 = int(input("Digite o número da sua escolha: "))
while escolha3 != 1 and escolha3 != 2:
    print("Opção inválida! Por favor, escolha 1 ou 2.")
    escolha3 = int(input("Digite o número da sua escolha: "))

if escolha3 == 1: 
    print("Você decide construir um abrigo.")
    perda4 = random.randint(15, 30)
    energia = energia - perda4
    print(f"Você perdeu {perda4} de energia. Energia restante: {energia}")
    print("Pela manhã, pescadores da ilha o encontram e decidem ajudá-lo.")
elif escolha3 == 2:
    print("Você decide acender uma fogueira.")
    perda5 = random.randint(5, 15)
    energia = energia - perda5
    print(f"Você perdeu {perda5} de energia. Energia restante: {energia}")
    print("Um navio distante vê a fumaça e envia uma equipe de resgate rapidamente. ")

#Resultado final
print(f"Sua energia final é: {energia}")
if energia < 30:
    print("O resgate chega, mas ele mal consegue levantar e até acha que o socorro é só mais um pesadelo.")
    print("(Final Surreal – Você foi resgatado, mas vai precisar de muitos cafés para voltar à vida normal!)")
elif energia >= 30 and energia <= 69:
    print("O resgate chega, mas você está tão fraco que mal consegue fazer uma piada.")
    print("(Final Irônico – Você sobreviveu, mas está mais parecendo um zumbi do que um herói.)")
else:
    print("O resgate chega e você está tão bem que dá até para dar autógrafos para os socorristas.")
    print("(Final Alegre – Você foi resgatado, e até parece que esteve em um spa por dias!)")