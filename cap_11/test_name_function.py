import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ Testes para 'name_function.py'. """


    # Nomes longos para os métodos em nossas classes 'TestCase' não são
    # um problema. Eles devem ser descritivos para que você possa compreender
    # a saída quando seus testes falaharem, e pelo fato de Python os 
    # chamar automaticamente, você não precisará escrever código para
    # chamar esses métodos.
    def test_first_last_name(self):
    # Qualquer método que comece com 'test_' será executado de modo
    # automático quando 'test_name_function.py' for executado.
        """ Nomes como 'Janis Joplin' funcionam? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


    def test_first_last_middle_name(self):
        """ Nomes como 'Wolfgang Amadeus Mozart' funcionam? """
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()