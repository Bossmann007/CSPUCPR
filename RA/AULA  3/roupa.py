print("Bem-vindo ao  sistema de recomnendação de roupas!")
print("Responda às perguntas para descobrir qual roupa usar.")
pergunta1=input("O evento é formal? {S/N} ")
resposta1=pergunta1.upper()
pergunta2=input("O evento é familiar? {S/N} ")
resposta2=pergunta2.upper()
pergunta3=input("O evento é na cidade? {S/N} ")
resposta3=pergunta3.upper()
pergunta4=input("Faz frio? {S/N} ")
resposta4=pergunta4.upper()
pergunta5=input("O local é aberto? {S/N} ")
resposta5=pergunta5.upper()
if resposta1=="S":
    respostafinal1="Use um terno ou um vestido longo,"
else:
    respostafinal1="Use uma roupa casual, como uma camisa e calça jeans ou um vestido curto,"
if resposta2=="S":
    respostafinal2="use algo confortável e apropriado para a família,"
else:    respostafinal2="opte por algo mais chamativo para causar impacto,"
if resposta3=="S":
    respostafinal3="lembre-se de usar sapatos confortáveis para caminhar na cidade,"
else:    respostafinal3="você pode usar sapatos mais elegantes para um evento em um local fechado,"
if resposta4=="S":
    respostafinal4="vista-se com camadas para se manter aquecido,"
else:    respostafinal4="opte por roupas mais leves para se manter fresco"
if resposta5=="S":
    respostafinal5="lembre-se de usar protetor solar e um chapéu para se proteger do sol."
else:    respostafinal5="você pode usar acessórios mais elegantes, como um chapéu ou uma bolsa de mão."
print("Recomendações de roupas:")
print(respostafinal1, respostafinal2, respostafinal3, respostafinal4, respostafinal5)
