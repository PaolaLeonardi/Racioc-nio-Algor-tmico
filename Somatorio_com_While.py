# Exercício 04

N = int(input ("Digite um número (N) para imprimir na tela o somatório dos primeiros números inteiros: "))
numero = 1
total = 0
expressao = ""

while numero <= N:
    total += numero

    if numero == 1:
        expressao += str(numero)
    else:
        expressao += " + " + str(numero)

    numero += 1

print(f"{expressao} = {total}")
