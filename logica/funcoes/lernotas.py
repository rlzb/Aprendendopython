from colorama import Fore

def lernotas():
    n = float(input("Digite uma nota para o aluno(a): "))
    return n

def resultado(n1, n2):
    media = (n1 + n2) / 2
    print(f"Nota 1 {n1}")
    print(f"Nota 2 {n2}")
    print("=" * 20)
    print(f"Sua Media Foi {media}")
    print("=" * 20)
    if media >= 7:
        print(Fore.GREEN + "+------------------+")        
        print("|     APROVADO     |")
        print("+------------------+" + Fore.RESET) 
    else:
        print(Fore.RED + "+------------------+")        
        print("|     REPROVADO    |")
        print("+------------------+" + Fore.RESET) 
        
a = lernotas()
b = lernotas()
resultado(a, b)