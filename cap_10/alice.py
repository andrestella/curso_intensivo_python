filename = "alice.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file '{}' does not exist.".format(filename)
    print(msg)
else:
    # Conta o número aproximado de palavras no arquivo
    words = contents.split() # o método 'split()' cria uma lista de palavras
    # a partir de uma string
    num_words = len(words)
    print("The file '{}' has about {} words.".format(filename, num_words))