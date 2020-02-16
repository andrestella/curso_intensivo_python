def show_magicians(magicos):
    """ Exibe os nomes de cada mágico de uma lista. """
    for magico in magicos:
        print(magico.title())

magicos = [
    'howard thurston',
    'david copperfield',
    'lance burton',
    'houdini',
    'david blaine',
    'dynamo',
    'derren brown',
    'criss angel'
    ]
show_magicians(magicos)