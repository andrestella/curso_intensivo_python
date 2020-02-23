""" Uma coleção de funções para trabalhar com cidades. """


def city_data(cidade, pais, populacao=''):
    """ Devolve os dados informados da cidade de forma elegante. """
    if populacao:
        cidade_dados = cidade + ", " + pais + " - população " + populacao
    else:
        cidade_dados = cidade + ", " + pais
    return cidade_dados.title()