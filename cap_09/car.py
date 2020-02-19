""" Um conjunto de classes usado para representar carro a combustível e elétricos. """
# Escreva uma docstring para cada módulo que criar


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


class Battery():
    """ Uma tentativa simples de modelar uma bateria para um carro elétrico. """


    def __init__(self, battery_size=70):
        """ Inicializa os atributos da bateria. """
        self.battery_size = battery_size


    def describe_battery(self):
        """ Exibe uma frase que exibe a capacidade da bateria. """
        print("This car has a {}-kWh battery.".format(self.battery_size))


    def get_range(self):
        """ Exibe uma frase sobre a distância que o carro é capaz de percorrer
        com essa bateria. """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = "Not specified"

        if range == "Not specified":
            message = "Battery not specified."
        else:
            message = "This car can go approximately " + str(range)
            message += " miles on a full charge."
        print(message)


    def upgrade_battery(self):
        """ Verifica a capacidade da bateria e faz um upgrade se o valor for diferente de 85. """
        if self.battery_size != 85:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")


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
        self.battery = Battery()
        # usando uma instância de 'Battery' como atributo da classe 'ElectricCar'
        # qualquer instância de 'ElectricCar' agora terá uma instância de 'Battery'
        # criada automaticamente


    # Sobrescrevendo métodos da classe-pai
    def fill_gas_tank(self):
        """ Carros elétricos não têm tanques de combustível. """
        print("This car doesn't need a gas tank!")