import pyfiglet
from time import sleep
from colorama import Fore

print(Fore.CYAN + "+-------------------------------------------------------------------+")
print(pyfiglet.figlet_format("TABUADA PRO"))
print("+-------------------------------------------------------------------+" + Fore.RESET)
print("=" * 38)
num = int(input("Digite Um Numero Para ver A Tabuada: "))
print("=" * 38)
print("=" * 15)
print("Carregando", end="", flush=True)

for i in range(3):
    sleep(1)
    print(".", end="", flush=True)
print()
print("=" * 15) 
print("{} x {} = {}".format(num, 1 ,num * 1))
print("{} x {} = {}".format(num, 2,num * 2 ))
print("{} x {} = {}".format(num, 3, num * 3))
print("{} x {} = {}".format(num, 4, num * 4))
print("{} x {} = {}".format(num, 5, num * 5))
print("{} x {} = {}".format(num, 6, num * 6))
print("{} x {} = {}".format(num, 7, num * 7))
print("{} x {} = {}".format(num, 8, num * 8))
print("{} x {} = {}".format(num, 9, num * 9))
print("{} x {} = {}".format(num, 10, num * 10))
print("=" * 15)
while True:
    continuar = str(input("Quer continuar?: ")).strip().upper()[0]
    if continuar == "S":
        numero = int(input("Digite um Numero para ver a tabuada: "))

        print("{} x {} = {}".format(numero, 1, numero * 1))
        print("{} x {} = {}".format(numero, 2, numero * 2))
        print("{} x {} = {}".format(numero, 3, numero * 3))
        print("{} x {} = {}".format(numero, 4, numero * 4))
        print("{} x {} = {}".format(numero, 5, numero * 5))
        print("{} x {} = {}".format(numero, 6, numero * 6))
        print("{} x {} = {}".format(numero, 7, numero * 7))
        print("{} x {} = {}".format(numero, 8, numero * 8))
        print("{} x {} = {}".format(numero, 9, numero * 9))
        print("{} x {} = {}".format(numero, 10, numero * 10))            
    else:
        print(Fore.GREEN +"FIM DO PROGRAMA, OBRIGADO POR UTILIZAR NOSSOS SERVICOS"+ Fore.RESET)
        break