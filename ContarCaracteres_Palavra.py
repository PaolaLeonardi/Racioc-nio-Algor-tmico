print ("Exercício 03")

palavra = input ("Palavra: ") # Pede pro usuário digitar algo e guarda na variável palavra

while len(palavra) <3 or len(palavra) >10: # len(palavra) = quantidade de caracteres da palavra
  print ("inválido")
  palavra = input ("Palavra: ") # Pede a palavra de novo (isso é essencial, senão o loop nunca muda o valor)

print (palavra, len(palavra))
