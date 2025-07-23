message = 'a kong string with a silly typo'# mensagem original  
nova_message = message.replace('kong', 'coffe') # kong substituido por coffe
print(nova_message) # printa a nova atualizacao
animals = 'lions tigers and bears'
print('horses' in animals) # return false
print("The number of times e occurs in this string is 4".count("e"))
"Mountains".upper()
"Mountains".lower()
answer =  "YES"
if answer.lower() == "yes":
    print("User said yes")
    print("yes".strip())
    print('yes'.lstrip())
    print("yes".rstrip())
print("Forrest".endswith('rest')) # mostra True
print("Forrest".isnumeric()) 
print("12345".isnumeric())
print(" ".join(['this', 'is', 'a', 'phrase', 'joined', 'by', 'spaces']))
print('...'.join(['this', 'is', 'a', 'phrase', ' joined', 'by', ' triple', 'dots']))
print('This is another example'.split())