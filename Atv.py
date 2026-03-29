print ("Exercício 03")

ano = int (input ("Diga um ano"))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Este ano é bissexto!")
else:
    print ("Este ano não é bissexto!")

print ("Exercício 04")

usuario = input("Digite o usuário:")

if usuario == "admin":
    print ("Bem vindo admin")
elif usuario == "convidado":
    print ("Acesso restrito")
else:
    print ("bloqueado")

senha = input ("Digite a senha:")
if senha == "1234":
    print ("Acesso autorizado, Bem vindo!")
else:
    print ("Acesso Bloqueado")

print ("Exercício 05")

cordenada1 = int (input ("Diga uma cordenada x"))
cordenada2 = int (input ("Diga uma cordenada y"))

if 0 < cordenada1 < 9 and 0 < cordenada2 < 9:
    print("Dentro do quadrado")
elif 0 <= cordenada1 <= 9 and 0 <= cordenada2 <= 9:
    print ("Na fronteira")
else:
    print ("Fora do quadrado")
