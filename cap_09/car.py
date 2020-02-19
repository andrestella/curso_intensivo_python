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


    def update_odometer(self, mileage):
        """ 
        Define o valor de leitura do hodômetro com o valor especificado.
        Rejeita a alteração se for tentativa de definir um valor menor para o hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        """ Soma a quantidade especificada ao valor de leitura do hodômetro. """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


    def fill_gas_tank(self):
        """ Simula o abastecimento de combustível. """
        print("Filling the tank...")


# Quando criamos uma classe-filha, a classe pai deve fazer parte do arquivo atual 
# e deve aparecer antes da classe-filha no arquivo.
class ElectricCar(Car):
    """ Representa aspectos de um carro específicos de veículos elétricos. """


    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico.
        """
        super().__init__(make, model, year)
        self.battery_size = 70


    def describe_battery(self):
        """ Exibe uma frase que exibe a capacidade da bateria. """
        print("This car has a {}-kWh battery.".format(self.battery_size))


    # Sobrescrevendo métodos da classe-pai
    def fill_gas_tank(self):
        """ Carros elétricos não têm tanques de combustível. """
        print("This car doesn't need a gas tank!")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modificando o valor de um atributo diretamente
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modificando o valor de um atributo com um método
my_new_car.update_odometer(50)
my_new_car.read_odometer()

# Incrementando o valor de um atributo com um método
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.read_odometer()

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_used_car.fill_gas_tank()

# Testando se a herança está funcionando 
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()