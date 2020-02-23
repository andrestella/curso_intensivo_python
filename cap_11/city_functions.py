""" Uma coleção de funções para trabalhar com cidades. """


def city_data(cidade, pais, populacao):
    """ Devolve o nome da cidade junto de seu país e população de forma elegante. """
    cidade_dados = cidade + ", " + pais + " - população " + populacao
    return cidade_dados.title()