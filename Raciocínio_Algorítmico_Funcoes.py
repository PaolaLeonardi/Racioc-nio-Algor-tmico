#A)
#1- Escreva uma função chamada "imprimir_nome" que imprime o seu nome.
def imprimir_nome(nome):
    return nome
nome = input("Diga seu nome")

print (imprimir_nome(nome))

#2 - Escreva uma função chamada "maior" que receba três números como parâmetros e
# retorne o maior entre eles.

def maior(x, y, z):
    if x <= y and z <= y:
        return y
    elif y <= x and z <= x:
        return x
    else:
        return z

x = int(input("Diga um número"))
y = int(input("Diga outro número"))
z = int(input("Diga o último número"))

print ("O maior número é:", maior(x, y, z))

#3 - Escreva uma função chamada "criar_vetor" que retorna um vetor preenchido com zeros
#de tamanho 5.
vetor = [0,0,0,0,0]

def criar_vetor():
    return vetor

print (criar_vetor())

#4 - Escreva uma função chamada "media" que receba uma lista de números
# como parâmetro e retorne a média desses números.

def media(lista):
    return sum(lista) / len(lista)

um = int(input("Diga um valor"))
dois = int(input("Mais outro valor"))
tres = int(input("último valor"))

lista=[um,dois,tres]

print (media(lista))

#5 - Escreva uma função chamada "inverter" que receba uma string
#como parâmetro e imprime a string invertida.

def inverter(string):
    return string[::-1] #significa “pegar a string de trás para frente”

valor = input("Diga uma palavra")

print (inverter(valor))

#6- Escreva uma função chamada "imprime_diagonal" que recebe uma matriz de tamanho
#3x3 preenchida com valores quaisquer, e imprime os valores na diagonal principal.

matriz = [
    [2,0,0,],
    [0,2,0,],
    [0,0,2,]
    ]

def imprime_diagonal(matriz):
    return matriz [0][0], matriz[1][1],matriz[2][2]

print (imprime_diagonal(matriz))

#B) 
#1 - Crie uma função chamada soma_elementos que receba uma lista de
#números como parâmetro e retorne a soma de todos os elementos dessa lista.

lista=[]
for i in range(5):
    
    valor = int(input("Diga um número:"))
    lista.append(valor)

def soma_elementos(lista):
    return sum(lista)

print(soma_elementos(lista))

#2- Crie uma função chamada e palindromo que receba uma string como
#parâmetro e retorne True se a string for um palíndromo (ou seja, se lida de trás
#para frente for igual à original) e False caso contrário.

def e_palindromo(string):
    if string == string[::-1]:
        return  True
    else:
        return  False

palavra = input("Digite uma palavra:")

print(e_palindromo(palavra))

#3- Crie uma função chamada maior_elemento que receba uma lista de números
#como parâmetro e retorne o maior elemento dessa lista.

def maior_elemento(lista):
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

#4- Crie uma função chamada contar_caracteres que receba uma string e um
#caractere como parâmetros e retorne o número de vezes que o caractere
#aparece na string

def contar_caracteres(string, caractere):
    return string.count(caractere)

texto = input("Digite uma palavra: ")
caractere = input("Digite um caractere: ")

print(contar_caracteres(texto, caractere))

#5- Implemente uma calculadora simples em Python utilizando funções. A
#calculadora deve ser capaz de realizar as seguintes operações
#matemáticas básicas:
#• Soma
#• Subtração
#• Multiplicação
#• Divisão
#Requisitos:
#• Crie uma função para cada operação matemática (soma,
#subtração, multiplicação e divisão). As funções devem receber
#dois valores e retornar o resultado da operação.
#• Implemente uma função para exibir o menu de opções para o
#usuário.
#• O programa deve repetir o menu após cada operação, até que
#o usuário escolha a opção de sai

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    return a / b

def menu():
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

while True:
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Programa encerrado.")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", soma(num1, num2))

    elif opcao == "2":
        print("Resultado:", subtracao(num1, num2))

    elif opcao == "3":
        print("Resultado:", multiplicacao(num1, num2))

    elif opcao == "4":
        print("Resultado:", divisao(num1, num2))

    else:
        print("Opção inválida.")
