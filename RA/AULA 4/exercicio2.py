soma = 0
contador = 0
num = int(input("Digite um valor: "))
while (num != 0):
    soma = soma + num
    contador = contador + 1
    num = int(input("Digite um valor: "))
if (contador > 0 ):
    media = soma / contador
    print(f"A média dos números digitados é: {media}")
else:
    print("Nenhum número foi digitado, média não calculada.")
