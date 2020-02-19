# Criando uma lista de linhas de um arquivo
filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
    # O método 'readlines()' armazena cada linha do arquivo em uma lista.

for line in lines:
    print(line.rstrip())