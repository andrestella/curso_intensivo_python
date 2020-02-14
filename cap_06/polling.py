favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

persons = ['andré', 'sarah', 'maria', 'phil', 'henri']

for person in persons:
    if person in favorite_languages.keys():
        print("{}, obrigado por respoder!".format(person.title()))
    else:
        print("{}, poderia nos responder a enquete?".format(person.title()))