soma = 0
contador = 0

while (contador < 5):
    num = input("Digite um valor: ")
    num = int(num)
    soma = soma + num
    contador = contador + 1

media = soma / 5

print(f"A média dos números digitados é: {media}")