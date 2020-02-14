cities = {
    'são paulo': {
        'país': 'brasil',
        'população': '12 milhões',
        'universidade': 'usp',
        },
    'curitiba': {
        'país': 'brasil',
        'população': '2 milhões',
        'universidade': 'ufpr',
        },
    'ribeirão preto': {
        'país': 'brasil',
        'população': '700 mil',
        'universidade': 'usp-rp',
        },
}

for cidade, cidade_info in cities.items():
    print("\nSegue informações acerca de {}:".format(cidade.title()))
    for info, dado in cidade_info.items():
        if info == 'universidade':
            dado = dado.upper()
        elif info == 'país':
            dado = dado.title()
        print("\t- {}: {}".format(info, dado))