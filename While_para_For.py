print ("Atividade 01")

#contador = 0
#while contador <= 10:
#   if contador % 2 != 0:
#       print (f“{contador} é ímpar.”)
#   else:
#       print(f“{contador} é par.”)
#contador = contador + 1

print ("De 1 a 10, par ou impar?")
for i in range(1,11): #O IN não funciona em outras linguagens
    if i == 0:
        continue #Para ignorar uma coisa expecífica, no caso o zero.

    if i % 2 != 0:
        print (f'{i} é impar!')
    else:
        print (f'{i} é par!')

print ("De 10 a 1")
for i in range (10,0,-1):
    print (i)

#Para printar cada letra de uma palavra:
# 1-> P, 2-> r, 3-> o,...

palavra = "profe"

for letra in palavra:
    print (letra)

print ("Atividade 02")

palavra = input ("Digite uma palavra que começe com uma vogal \n > ")

if palavra[0].lower() not in "aeiou": #o [0] pega a primeira letra de "Palavra"
    # in verifica se algo está dentro
    # not in verifica de algo não está dentro
    # .lower() Faz com que inclua letras maiúsculas
    # ['P', 'a','l', 'a', 'v', 'r','a'] 
    # Dá p/ fzer usando while
    print ("Palavra Inválida!")
else:
    for letra in palavra:
        print(letra)

print ("Atividade 03")

for linha in range (3):
    for coluna in range (4):
        print ("*", end = " ") # (E)ND, não o (A)ND
    print ()
        print (i)
# Ele prioriza o FOR de dentro primeiro se tiver dois IN
