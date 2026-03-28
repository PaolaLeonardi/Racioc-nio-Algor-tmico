print ("Exercício 01") # Esse código gera uma lista de 1 a 10

numero = 1  
while numero <= 10:
  print (numero)
  numero = numero +1
  
print ("Exercício 02") # Esse código gera uma lista de 10 a 0

numero = 10  
while numero > 0:
  print (numero)
  numero -=1

print ("Exercício 03")

palavra = input ("Palavra: ") # Pede pro usuário digitar algo e guarda na variável palavra

while len(palavra) <3 or len(palavra) >10: # len(palavra) = quantidade de caracteres da palavra
  print ("inválido")
  palavra = input ("Palavra: ") # Pede a palavra de novo (isso é essencial, senão o loop nunca muda o valor)

print (palavra, len(palavra))

print ("Exercício 03") # Pede um número de 0 a 10 e só aceita quando o valor é válido

numero = int(input("Estudante, digite um número de 0 a 10"))

while numero > 10 or numero < 0: # Ou posso usar 0 < numero < 10 se preferir (no pyton)
    print ("Inválido, digite uma número de 0 a 10")
    numero = int(input("Digite um número de 0 a 10: ")) # Repete

print (f"sua nota é {numero}") # Dentro de {} você coloca a variável direto

#Proximos ex. a fazer: ----------------------------------------------------

#4.Implemente um programa em Python para imprimir na tela o somatório dos N primeiros números inteiros a partir do 1. Sendo N lido do teclado;
#5. Implemente um programa em Python para ler do teclado números. Caso o usuário forneça um número igual a -1, o programa deve fornecer a média dos números e encerrar;
#6. Escreva um programa que receba 10 números do teclado e exiba a quantidade de números pares e ímpares lidos.
