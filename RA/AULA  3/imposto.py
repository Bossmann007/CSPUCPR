salario=float(input("Digite o valor do salário:  R$"))
if salario>0 and salario<=1903.98:
    print("Isento de imposto de renda.")
else: 
    if salario<=2826.65:
       imposto=salario*0.075       
    elif salario<=3751.05:  
        imposto=salario*0.15              
    elif salario<=4664.68:         
        imposto=salario*0.225                
    else:
        imposto=salario*0.275
print(f"O valor do imposto de renda é: R${imposto:.2f}.")