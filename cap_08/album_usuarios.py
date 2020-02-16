def make_album(artista, titulo, faixas=''):
    """ Devolve um dicionário com o nome do artista, nome do album e o n° de faixas (opcional). """
    album = {
        'artista': artista,
        'titulo': titulo,
        }
    if faixas:
        album['faixas'] = faixas
    return album

while True:
    print("\nForneça os dados da sua banda favorita.")
    print("Digite 'sair' a qualquer momento se desejar parar.")
    artista = input("Digite o nome da banda: ")
    if artista == 'sair':
        break
    album = input("Digite o nome do álbum: ")
    if album == 'sair':
        break
    faixas = input("N° de faixas do álbum (opcional): ")
    if faixas == 'sair':
        break
    if faixas:
        artista_album = make_album(artista, album, faixas)
        print(artista_album)
    else:
        artista_album = make_album(artista, album)
        print(artista_album)