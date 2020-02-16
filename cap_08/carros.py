def mostra_carro(fabricante, modelo, **info_adicionais):
    """ Exibe as características de um determinado modelo de carro. """
    características = {
        'fabricante': fabricante,
        'modelo': modelo,
        }
    for key, valor in info_adicionais.items():
        características[key] = valor
    for key, valor in características.items():
        print("- {}: {}".format(key, valor))

mostra_carro('subaru', 'outback', color='blue', tow_package=True)
print("\n")
mostra_carro('honda', 'accord', year=1991, color='white',
    headlights='popup')