""" Uma coleção de funções para trabalhar com cidades. """


def city_data(cidade, pais):
    """ Devolve o nome da cidade junto de seu país de forma elegante. """
    cidade_pais = cidade + ", " + pais
    return cidade_pais.title()