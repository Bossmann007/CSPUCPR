nota1=float(input("Digite a primeira nota:"))
nota2=float(input("Digite a segunda nota:"))
nota3=float(input("Digite a terceira nota:"))
media=(nota1+nota2+nota3)/3
if media >=9.0:
    conceito="A"
elif media >=7.5:
    conceito="B"
elif media >=6.5:
    conceito="C"
elif media >=4.0:
    conceito="D"
else:
    conceito="E"
print(f"A média do aluno é:{media:.1f} e o conceito é: {conceito}.") 
if media >=7.0:
   print("Status: Aprovado")
else:
   print("Status: Reprovado")