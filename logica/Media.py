notaA = float(input("Informe a Primeira Nota: "))
notaB = float(input("informe a Segunda Nota: "))

#Calcular media
mediafinal = (notaA + notaB) / 2

#Verificar if aprovado or reprovado
if mediafinal >= 7.0:
    print(f"APROVADO COM {mediafinal}, PARABENS")
else:
    print(f"REPROVADO COM {mediafinal}, ESTUDE MAIS!!!")