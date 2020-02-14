person_0 = {
    'first_name': 'andré',
    'last_name': 'stella',
    'age': 70,
    'city': 'ribeirão preto',
}
person_1 = {
    'first_name': 'maria',
    'last_name': 'stella',
    'age': 60,
    'city': 'são paulo',
}
person_2 = {
    'first_name': 'alexandre',
    'last_name': 'stella',
    'age': 40,
    'city': 'são paulo',
}

people = [person_0, person_1, person_2]

for person in people:
    print(person['first_name'].title())
    print(person['last_name'].title())
    print(person['age'])
    print(person['city'].title() + "\n")