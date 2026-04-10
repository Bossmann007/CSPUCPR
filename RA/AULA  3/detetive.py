print("Bem-vindo ao jogo de detetive!")
print("Responda às perguntas para descobrir o assassino.")
pergunta1=input("Telefonou para a vítima? {S/N} ")
resposta1=pergunta1.upper()
pergunta2=input("Esteve no local do crime? {S/N} ")
resposta2=pergunta2.upper()
pergunta3=input("Mora perto da vítima? {S/N} ")
resposta3=pergunta3.upper()
pergunta4=input("Devia para a vítima? {S/N} ")
resposta4=pergunta4.upper()
pergunta5=input("Já trabalhou com a vítima? {S/N} ")
resposta5=pergunta5.upper()
respostaspositivas=0
if resposta1=="S":
    respostaspositivas+=1
if resposta2=="S":
    respostaspositivas+=1
if resposta3=="S":
    respostaspositivas+=1
if resposta4=="S":
    respostaspositivas+=1
if resposta5=="S":
    respostaspositivas+=1
if respostaspositivas==2:
    print("Suspeita!")
elif respostaspositivas>=3 and respostaspositivas<=4:
    print("Cúmplice!")
elif respostaspositivas==5:
    print("Assassino!")
else:    print("Inocente!")