print ("Exercício 01")

#Faça um programa que percorra os números de 1 até 100 e mostre apenas aqueles que
#são múltiplos de 3 e, ao mesmo tempo, não são múltiplos de 5. Ao final, mostre também
#quantos números atenderam a essa condição.

numero = 0
for i in range (1,101):
    if i %3 == 0 and i %5 != 0:
        print (i)
        numero += 1
print ("Quantidade de números é:", numero)

print ("Exercício 02)

#Peça ao usuário um número inteiro positivo n. Não permita que o programa continue
#caso o número não seja válido. Em seguida, calcule e exiba a soma de todos os números
#de 1 até n. Ao final exiba a expressão aritmética completa, incluindo o resultado.
#Exemplo: n = 5 -> Output: 1 + 2 + 3 + 4 + 5 = 15

N = int (input ("Diga um número inteiro positivo \n> "))
while N <0:
    print ("Número inválido")
    N = int (input ("Diga um número inteiro positivo \n> "))

total = 0
espaco= ""

for i in range (1, N+1):
    total += i

    if i == 1:
        espaco += str(i) #Trasnformo p/ string
    else:
        espaco += "+" + str(i)
print (f"{espaco} = {total}")
