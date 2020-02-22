filenames = ['cats.txt', 'dogs2.txt']

for filename in filenames:
    try:        
        with open(filename) as arquivo:
            conteudo = arquivo.read()            
    except FileNotFoundError:
        pass
    else:
        print("\nConteúdo do arquivo '{}':".format(filename))
        print(conteudo)
