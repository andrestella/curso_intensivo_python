""" Uma coleção de funções para trabalhar com cidades. """


def city_data(cidade, pais, populacao=''):
    """ Devolve os dados informados da cidade de forma elegante. """
    cidade_pais = (cidade + ", " + pais).title()
    if populacao:
        cidade_dados = cidade_pais + " - população " + str(populacao)
    else:
        cidade_dados = cidade_pais
    return cidade_dados