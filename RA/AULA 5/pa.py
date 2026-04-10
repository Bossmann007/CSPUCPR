a1 = float (input ("Digite um valor de a1: "))
razao = float (input ("Digite a razao: "))
n = int (input ("Digite o numero de termos desejado: "))
at = a1
for i in range (1, n):
    print(i,at)
    at *= razao
print(f"O valor do {n} termo da progressao a é {at:.2f}")

