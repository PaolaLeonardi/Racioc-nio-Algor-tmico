#Faca um programa que possua um vetor denominado A que armazene 6 numeros intei-ros.
#O programa deve executar os seguintes passos:
#(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
#(b) Armazene em uma variavel inteira (simples) a soma entre os valores das posicoes
#A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
#(c) Modifique o vetor na posicao 4, atribuindo a esta posicao o valor 100.
#d) Mostre na tela cada valor do vetor A, um em cada linha.
A = [1,0,5,-2,-5,7]
soma = A[0]+A[1]+A[5]
print (soma)
A[4] = 100
print (A)

#Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos:
valores=[]

print ("Diga 6 valores inteiros:")

for i in range (0,6):
    valor = (int(input("Valor:\n>")))
    valores.append(valor)
print (valores)
