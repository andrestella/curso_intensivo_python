import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ Testes para 'name_function.py'. """


    def test_first_last_name(self):
    # Qualquer método que comece com 'test_' será executado de modo
    # automático quando 'test_name_function.py' for executado.
        """ Nomes como 'Janis Joplin' funcionam? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()