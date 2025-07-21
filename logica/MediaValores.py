qtd = 0
soma = 0
media = 0
valor = float(input("Digite Um Valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd +1
    # Entrada De Valores
    valor = float(input("Digite Um valor: "))
    
# Caso Digite um valor negativo o laco encerra
media = soma / qtd
print(f"\n TOTAL DA SOMA {soma}")
print(f"\n QUANTIDADES DE VALORES DIGITADOS {qtd} ")
print(f"\n MEDIA DOS VALORES {media:.2f}")