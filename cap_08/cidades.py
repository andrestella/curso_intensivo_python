def describe_city(cidade, pais='brasil'):
    """ Descreve uma cidade e em qual país está localizada. """
    print("{} está localizada no {}.".format(cidade.title(), pais.title()))

describe_city('são paulo')
describe_city(cidade='curitiba')
describe_city('santiago', 'chile')