valori = float (input ("Digite um valor: "))
taxaj = float (input ("Digite a taxa de juros: "))
anos = int (input ("Digite o numero de anos: "))

valorf = valori
for i in range (0,anos,):
    valorf *= (1 + taxaj)
print(f"O valor final do investimento em {anos} é {valorf:.2f}")
