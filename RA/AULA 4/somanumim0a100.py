soma = 0
num = 1
while (num <= 100):
    if (num % 2 != 0):
        soma += num
    num += 1    
print(f"Soma dos numeros impares de 1 a 100: {soma}")