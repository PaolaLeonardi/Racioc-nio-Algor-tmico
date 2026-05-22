def main():

    # A)

    def um():
        def imprimir_nome(nome):
            return nome

        nome = input("Diga seu nome: ")
        print(imprimir_nome(nome))


    def dois():
        def maior(x, y, z):
            if x <= y and z <= y:
                return y
            elif y <= x and z <= x:
                return x
            else:
                return z

        x = int(input("Diga um número: "))
        y = int(input("Diga outro número: "))
        z = int(input("Diga o último número: "))

        print("O maior número é:", maior(x, y, z))


    def tres():

        def criar_vetor():
            return [0, 0, 0, 0, 0]

        print(criar_vetor())


    def quatro():

        def media(lista):
            return sum(lista) / len(lista)

        n1 = int(input("Diga um valor: "))
        n2 = int(input("Mais outro valor: "))
        n3 = int(input("Último valor: "))

        lista = [n1, n2, n3]

        print(media(lista))


    def cinco():

        def inverter(string):
            return string[::-1]

        valor = input("Diga uma palavra: ")

        print(inverter(valor))


    def seis():

        matriz = [
            [2, 0, 0],
            [0, 2, 0],
            [0, 0, 2]
        ]

        def imprime_diagonal(matriz):
            return matriz[0][0], matriz[1][1], matriz[2][2]

        print(imprime_diagonal(matriz))


    # B)

    def umB():

        lista = []

        for i in range(5):
            valor = int(input("Diga um número: "))
            lista.append(valor)

        def soma_elementos(lista):
            return sum(lista)

        print(soma_elementos(lista))


    def doisB():

        def e_palindromo(string):
            return string == string[::-1]

        palavra = input("Digite uma palavra: ")

        print(e_palindromo(palavra))


    def tresB():

        def maior_elemento(lista):

            maior = lista[0]

            for numero in lista:
                if numero > maior:
                    maior = numero

            return maior

        lista = [1, 5, 9, 2, 7]

        print(maior_elemento(lista))


    def quatroB():

        def contar_caracteres(string, caractere):
            return string.count(caractere)

        texto = input("Digite uma palavra: ")
        caractere = input("Digite um caractere: ")

        print(contar_caracteres(texto, caractere))


    def cincoB():

        def somar(x, y):
            return x + y

        def subtrair(x, y):
            return x - y

        def multiplicar(x, y):
            return x * y

        def dividir(x, y):
            if y == 0:
                return "Erro: divisão por zero!"
            else:
                return x / y

        def menu():
            print("\n=== CALCULADORA ===")
            print("1 - Somar")
            print("2 - Subtrair")
            print("3 - Multiplicar")
            print("4 - Dividir")
            print("5 - Sair")

        while True:

            menu()

            opcao = input("Selecione uma opção: ")

            if opcao == "5":
                print("Encerrando a calculadora...")
                break

            x = int(input("Qual o primeiro número: "))
            y = int(input("Qual o segundo número: "))

            if opcao == "1":
                resultado = somar(x, y)

            elif opcao == "2":
                resultado = subtrair(x, y)

            elif opcao == "3":
                resultado = multiplicar(x, y)

            elif opcao == "4":
                resultado = dividir(x, y)

            else:
                print("Opção inválida")
                continue

            print(f"Resultado: {resultado}")


    # Chamando as funções

    um()
    dois()
    tres()
    quatro()
    cinco()
    seis()

    umB()
    doisB()
    tresB()
    quatroB()
    cincoB()


main()
