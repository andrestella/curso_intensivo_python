# Importando um módulo completo
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# A opção abaixo:
# from car import *
# também vai importar todas as classes do módulo, mas não é um método recomendado