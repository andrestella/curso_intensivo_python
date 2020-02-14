favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("{}'s favorite languages are:".format(name.title()))
        for language in languages:
            print("\t- " + language.title())
    elif len(languages) == 1:
        print("{}'s favorite language is:\n\t- {}"
            .format(name.title(), languages[0].title()))