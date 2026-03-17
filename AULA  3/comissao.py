valorv=float(input("Digite o valor da venda:"))
if valorv <=100:
    comissao=valorv*0.05
elif valorv <=500:
    comissao=valorv*0.06
elif valorv <=1000:
    comissao=valorv*0.07
else:
    comissao=valorv*0.08
print(f"O valor da comissão é: {comissao:.2f} R$.")