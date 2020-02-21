def count_words(filename):
    """ Conta o número aproximado de palavras em um arquivo. """
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # Escreve o nome dos arquivos ausentes no arquivo 'missing_files.txt'.
        with open('missing_files.txt', 'a') as f_obj:
            f_obj.write(filename + "\n")
    else:
        words = contents.split()
        num_words = len(words)
        print("The file '{}' has about {} words.".format(filename, num_words))    

filenames = ["alice.txt", "siddhartha2.txt", "moby_dick2.txt", "little_women.txt"]
for filename in filenames:
    count_words(filename)