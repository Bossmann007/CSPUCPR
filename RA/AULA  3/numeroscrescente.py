n1=float(input("Digite o primeiro número: "))
n2=float(input("Digite o segundo número: "))
n3=float(input("Digite o terceiro número: "))
if n1<=n2 and n2<=n3:
    print(f"Os números em ordem crescente são: {n1:.2f}, {n2:.2f} e {n3:.2f}.")
elif n1<=n3 and n3<=n2:
    print(f"Os números em ordem crescente são: {n1:.2f}, {n3:.2f} e {n2:.2f}.")
elif n2<=n1 and n1<=n3:
    print(f"Os números em ordem crescente são: {n2:.2f}, {n1:.2f} e {n3:.2f}.")
elif n2<=n3 and n3<=n1:
    print(f"Os números em ordem crescente são: {n2:.2f}, {n3:.2f} e {n1:.2f}.")
elif n3<=n1 and n1<=n2:
    print(f"Os números em ordem crescente são: {n3:.2f}, {n1:.2f} e {n2:.2f}.")
else:    
    print(f"Os números em ordem crescente são: {n3:.2f}, {n2:.2f} e {n1:.2f}.")