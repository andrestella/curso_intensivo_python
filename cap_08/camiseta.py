def make_shirt(tamanho, texto):
    """ Verificar o tamanho e a mensagem a ser estampada na camiseta. """
    print('A camiseta de tamanho {} será estampada com a seguinte mensagem: "{}".'
        .format(tamanho.upper(), texto.title()))

make_shirt('gg', 'eu amo python!')
make_shirt(texto = 'funções em python!', tamanho = 'p')

def make_shirt(tamanho = 'g', texto = 'eu amo python!'):
    """ Verificar o tamanho e a mensagem a ser estampada na camiseta. """
    print('A camiseta de tamanho {} será estampada com a seguinte mensagem: "{}".'
        .format(tamanho.upper(), texto.title()))

make_shirt()
make_shirt('m')
make_shirt('p', 'vamos estudar!')