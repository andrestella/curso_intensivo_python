numero = input("Informe um número: ")
numero = int(numero)

if numero % 10 == 0:
    print("O número {} é múltiplo de 10!".format(numero))
else:
    print("O número {} não é múltiplo de 10!".format(numero))