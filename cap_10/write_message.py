# Escrevendo dados em um arquivo vazio
filename = "programming.txt"

with open(filename, 'w') as file_object:
# A função 'open()' cria o arquivo caso ele ainda não exista.
# Ao abrir um arquivo em modo de escrita ('w'), Python o apagará antes de 
# devolver o objeto arquivo.
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# Podemos abrir um arquivo em:
#  - modo de leitura ('r')
#  - modo de escrita ('w')
#  - modo de concatenação ('a')
#  - modo que permita ler e escrever no arquivo ('r+')
# Se o argumento de modo for omitido, o padrão é o modo de leitura ('r').

# Python escreve apenas strings em um arquivo-texto. Se quiser armazenar dados
# numéricos em um arquivo-texto, será necessário converter os dados em um
# formato de string antes usando a função 'str()'.

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)