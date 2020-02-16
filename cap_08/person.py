def build_person(first_name, last_name, age=''):
    """ Devolve um dicionário con informações sobre uma pessoa. """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print(build_person('andré', 'stella', 40))