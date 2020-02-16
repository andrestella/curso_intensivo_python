def make_album(artista, titulo, faixas=''):
    """ Devolve um dicionário com o nome do artista, nome do album e o n° de faixas (opcional). """
    album = {
        'artista': artista,
        'titulo': titulo,
        }
    if faixas:
        album['faixas'] = faixas
    return album

album = make_album('bon jovi', 'these days', 14)
print(album)

album = make_album('iron maiden', 'brave new world')
print(album)

album = make_album('engenheiros do hawaii', 'o papa é pop')
print(album)