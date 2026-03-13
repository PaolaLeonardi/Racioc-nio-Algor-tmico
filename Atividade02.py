print ('Exercício 01') # → serve para mostrar algo na tela

nascimento = input ('Qual sua data de nascimento?') # o input pede para o usuário digitar algo, esse algo vai se tornar a variável
print () # apenas para pular uma linha
ano_atual= 2026 # Define que a variável ano_atual seja igual a 2026
idade= int (ano_atual) - int (nascimento)

# int converte os valores para números inteiros, o nascimento era frase mas deve ser um número agora.
# idade = ano_atual menos nascimento.

# VARIÁVEL = Pode assumir qualquer valor
# CONSTANTE = Não muda

print ('Exercício 02')

carro= float (100.00)
# Real -> Float

quantidade = input ('Quantos carros gostaria de comprar?')
valor_total = (int (quantidade) * int (carro))
print (f" O valor dos carros fica: {valor_total} reais")
# o F antes das aspas deixa colocar variáveis dentro do texto

print ('Exercício 03')

celcius = input ('Diga uma temperatura em Celsius')
print ()

Fahrenheit= int (celcius) * 9/5 + 32
print ( f" temperatura em Fahrenheit: {int(Fahrenheit)}")

# Usar o {int()} faz com que o valor final fique sem o .0

print ('Exercício 04')

Nota1= input ("Qual sua primeira nota?")
Nota2= input ("Qual sua segunda nota?")
Nota3= input ("Qual sua terceira nota?")
Nota4= input ("Qual sua quarta nota?")

Soma= (int (Nota1) + int (Nota2) + int (Nota3) + int (Nota4))
print (f" Sua nota final é {int (Soma) / 4 }")

print ('Exercício 05')

Ano_Atual= 2026

nascimento = int (input ("Qual o ano do seu nascimento?"))

Idade = Ano_Atual - nascimento
idade_meses= Idade * 12

print (f"Sua idade em meses seria: {idade_meses}")
