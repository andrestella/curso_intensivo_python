import unittest
from city_functions import city_data


class CitiesTestCase(unittest.TestCase):
    """ Testes para 'city_functions.py'. """


    def test_city_country(self):
        """ Cidades como Santiago no Chile funcionam? """
        cidade_pais = city_data('santiago', 'chile')
        self.assertEqual(cidade_pais, 'Santiago, Chile')


unittest.main()