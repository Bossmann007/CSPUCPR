n = int (input ("Digite um numero inteiro: "))
fatorial = 1
for i in range (1, n+1):
    fatorial *= i  
print(f"O fatorial de {n} é {fatorial}")

if n == 0:
    print(f"O fatorial de {n} é 1")