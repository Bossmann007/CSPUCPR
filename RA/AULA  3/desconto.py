valor=float(input("Digite o valor do produto: "))
if valor>0 and valor<=2000:
    desconto=valor*0.03
    valorf=valor-desconto
elif valor>2000 and valor<=3000:
    desconto=valor*0.045
    valorf=valor-desconto
elif valor>3000 and valor<=5000:
    desconto=valor*0.05
    valorf=valor-desconto
elif valor>5000 and valor<=7000:
    desconto=valor*0.06
    valorf=valor-desconto
elif valor>7000:
    desconto=valor*0.07
    valorf=valor-desconto
else:
    print("Valor inválido")
print("O valor final do  produto é:",valorf,"R$.")
print("O desconto aplicado é:",desconto,"R$.")