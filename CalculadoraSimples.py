print ("\n 1: soma, 2: subtração, 3: multiplicação, 4: divisão, 0: sair")

while True:
    tres = input ("Informe a operação: \n> ")

    if tres == "0":
        print("Operação encerrada")
        break

    um = float (input("Informe o primeiro número: \n> "))
    dois = float (input("Informe o segundo número: \n> "))

    if tres == "1":
        print (um + dois)

    elif tres == "2":
        print (um - dois)

    elif tres == "3":
        print(um * dois)

    elif tres == "4":
        if dois != 0:
            print(um / dois)
        else:
            print("Não pode dividir por zero")

    else:
        print("Opção inválida")

print("1: soma, 2: subtração, 3: multiplicação, 4: divisão, 0: sair")
