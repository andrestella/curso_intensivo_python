# Lendo um arquivo inteiro
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip()) 
    # A única diferença entre essa saída e o arquivo original é uma linha
    # em branco extra no final da saída. A linha em branco aparece porque
    #'read()' devolve uma string vazia quando alcança o final do arquivo.
    # Se quiser remover essa linha em branco extra, 'rstrip()' pode ser usada.