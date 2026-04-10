somapar = 0
somaimpar = 0
somamult5 = 0 
num = 0
while (num <= 100):
    if (num % 2 == 0):
        print(f"{num} eh par")
        somapar += num
    else:
        print(f"{num} eh impar")
        somaimpar += num

    if (num % 5 == 0):
        somamult5 += num
    num += 1
print(f"Soma dos numeros pares: {somapar}")
print(f"Soma dos numeros impares: {somaimpar}")
print(f"Soma dos numeros multiplos de 5: {somamult5}")