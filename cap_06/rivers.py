rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print("The {} flows through {}.".format(river.title(), country.title()))

print("\n")

for river in rivers.keys():
    print("- " + river.title())

print("\n")

for country in set(rivers.values()):
    print("- " + country.title())