def formata(valor):
    if valor == True:
        return "V"
    return "F"

print("P | Q | R | S | P∨Q | ¬(P∨Q) | ¬S∧S | Resultado")
print("-" * 55)

for P in [True, False]:
    for Q in [True, False]:
        for R in [True, False]:
            for S in [True, False]:
                PouQ = P or Q
                nPouQ = not PouQ
                nSandS = not S and S
                resultado = not nPouQ or nSandS
                print(f"{formata(P)} | {formata(Q)} | {formata(R)} | {formata(S)} | {formata(PouQ)} | {formata(nPouQ)} | {formata(nSandS)} | {formata(resultado)}")