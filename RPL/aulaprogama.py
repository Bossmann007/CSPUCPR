#Problema:Sistema se decide se um estuadante pode acessar um laboratorio
import datetime
print("Bem Vindo ao Laboratorio de Informatica da PUCPR")
if datetime.datetime.now().hour >= 8 and datetime.datetime.now().hour <= 18:
    print("O laboratorio esta aberto, por favor faça seu login") 
    Login=(input("Digite seu Login:"))
    Senha=(input("Digite sua Senha:"))
    if Login == ("PUCPR") and Senha == ("SENHA"):
        print("Login valido!")
    else:
        print("Acesso negado")
else:
    print("O laboratorio esta fechado, por favor tente novamente mais tarde")
