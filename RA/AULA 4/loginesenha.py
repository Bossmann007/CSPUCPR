cont = 1
user = "admin"
senha = "1234"
us = input("Digite o nome de usuario: ")
pss = input("Digite a senha: ")
while (us != user or pss != senha) and cont <= 3:
    print("Usuario ou senha incorretos, tente novamente")
    us = input("Digite o nome de usuario: ")
    pss = input("Digite a senha: ")
    cont += 1
if (us == user and pss == senha):
    print("Login realizado com sucesso")
else:
    print("Numero maximo de tentativas excedido")