class Car():
    """ Uma tentativa simples de representar um carro. """


    def __init__(self, make, model, year):
        """ Inicializa os atributos que descrevem um carro. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # definindo um valor default para um atributo
        # você não precisará incluir um parâmetro para ele


    def get_descriptive_name(self):
        """ Devolve um nome descritivo, formatado de modo elegante. """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """ Exibe uma frase que mostra a milhagem do carro. """
        print("This car has {} miles on it.".format(self.odometer_reading))


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()