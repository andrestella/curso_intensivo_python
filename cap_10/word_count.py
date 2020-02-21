def count_words(filename):
    """ Conta o número aproximado de palavras em um arquivo. """
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file '{}' does not exist.".format(filename)
        # print(msg)
        pass # falhando silenciosamente
        # A instrução 'pass' também atua como um marcador. É um lembrete 
        # de que você optou por não fazer nada em um ponto específico da 
        # execução de seu programa, mas talvez queira fazer algo nesse local,
        # no futuro.
    else:
        words = contents.split()
        num_words = len(words)
        print("The file '{}' has about {} words.".format(filename, num_words))    

# filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]
filenames = ["alice.txt", "siddhartha2.txt", "moby_dick.txt", "little_women.txt"]
for filename in filenames:
    count_words(filename)