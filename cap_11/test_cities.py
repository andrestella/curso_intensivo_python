import unittest
from city_functions import city_data


class CitiesTestCase(unittest.TestCase):
    """ Testes para 'city_functions.py'. """


    def test_city_country(self):
        """ Cidades como Santiago no Chile funcionam? """
        cidade_pais = city_data('santiago', 'chile')
        self.assertEqual(cidade_pais, 'Santiago, Chile')


    def test_city_country_population(self):
        """
        Cidades como Santiago no Chile com população de 500000
        habitantes funcionam?
        """
        cidade_dados = city_data('santiago', 'chile', 500000)
        self.assertEqual(cidade_dados, 'Santiago, Chile - população 500000')


unittest.main()