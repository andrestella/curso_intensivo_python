import unittest
from funcionario import Employee


class TestEmployee(unittest.TestCase):
    """ Testes para a classe Employee. """


    def setUp(self):
        """ Cria uma instância da classe para ser utilizada nos testes. """
        self.empregado = Employee('andre', 'stella', 300000)


    def test_give_default_raise(self):
        """ Testa se a soma do valor padrão ao salário anual está correta. """
        self.empregado.give_raise()
        self.assertEqual(305000, self.empregado.annual_salary)


    def test_give_custom_raise(self):
        """ Testa se a soma de um determinado valor ao salário anual está correta. """
        self.empregado.give_raise(10000)
        self.assertEqual(310000, self.empregado.annual_salary)    


unittest.main()