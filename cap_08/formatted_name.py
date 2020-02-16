# Deixando um argumento opcional
def get_formatted_name(first_name, last_name, middle_name=''):
    """ Devolve um nome completo formatado de modo elegante. """
    if middle_name: # Python interpreta strings não vazias como 'True'
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

print(get_formatted_name('andré', 'stella', 'alexandre'))
print(get_formatted_name('andré', 'stella', middle_name='alexandre'))