filenames = ['cats.txt', 'dogs2.txt']

for filename in filenames:
    try:
        print("\nConteúdo do arquivo '{}':".format(filename))
        with open(filename) as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado!".format(filename))