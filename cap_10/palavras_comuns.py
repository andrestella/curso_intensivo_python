filenames = ['descartes.txt', 'newton.txt', 'leibniz.txt']
palavra_procurada = 'the'

for filename in filenames:
    try:        
        with open(filename) as arquivo:
            conteudo = arquivo.read()            
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado!".format(filename))    
    else:
        qtde_palavras = conteudo.lower().count(palavra_procurada)
        # O método 'count()' verifica quantas vezes determinada palavra
        # aparece em um texto.
        # Converter a string para letras minúsculas usando 'lower()' faz
        # com que todas as formas da palavra que está procurando sejam
        # capturadas.
        print("\nA palavra '{}' aparece {} vezes no arquivo '{}'."
            .format(palavra_procurada, qtde_palavras, filename))