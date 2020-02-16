def city_country(cidade, pais):
    """ Devolve o nome da cidade e seu país formatado de modo elegante. """
    cidade_pais = cidade.title() + ", " + pais.title()
    return cidade_pais

print(city_country('santiago', 'chile'))
print(city_country('são paulo', 'brasil'))
print(city_country('buenos aires', 'argentina'))