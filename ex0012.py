preco = float(input("Digite o Valor para obter o desconto? R$"))
novo = preco - (preco * 5 /100)
print(f"o produto que custava R${preco:.2f}, Com Desconto de 5% vai custar R${novo}")