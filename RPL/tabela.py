def formata(valor):
    if valor == True:
        return "V"
    return "F"

def negacao(p):
    return not p

def conjuncao(p, q):
    return p and q

def disjuncao(p, q):
    return p or q

def implicacao(p, q):
    if p and not q:
        return False
    return True

def bicondicional(p, q):
    if p != q:
        return False
    return True

print("p     | q     | p∧q  | p∨q  | p→q  | p↔q")
print("-" * 50)

for P in [True, False]:
    for Q in [True, False]:
        for R in [True, False]:
            for S in [True, False]:
                resultado = (not (P or Q)) and (not (not P and R)) and (not S and S)
                print(f"{formata(P)} | {formata(Q)} | {formata(R)} | {formata(S)} | {formata(resultado)}")
resultados = []

for p in [True, False]:
    for q in [True, False]:
        resultado = # sua fórmula aqui
        resultados.append(resultado)