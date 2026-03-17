l=int(input("Digite a largura desejada:"))
c=int(input("Digite o comprimento desejado:"))
p=int(input("Digite o numero de pavimentos:"))
a=l*c
if p>1:a=(l*c*p)
else:a=(l*c)
print("Area:",a,"metros quadrados")
