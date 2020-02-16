def show_magicians(magicos):
    """ Exibe os nomes de cada mágico de uma lista. """
    for magico in magicos:
        print(magico.title())

def make_great(magicos):
    """ Acrescenta a expressão "o grande" ao nome de cada mágico. """
    grandes_magicos = ["o grande " + magico for magico in magicos]
    return grandes_magicos

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

show_magicians(make_great(magicos))

print("\n")

print(magicos)
print(make_great(magicos))