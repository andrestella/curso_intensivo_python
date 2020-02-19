# Lendo dados linha a linha
filename = "pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        # A instrução 'print' adiciona a sua própria quebra de linha sempre 
        # que a chamamos, portanto acabamos com dois caracteres de quebra
        # de linha no final de cada linha: um do arquivo e outro da instrução
        # 'print'. Se usarmos 'rstrip()' em cada linha na instrução 'print',
        # eliminamos essas linhas em branco extras.