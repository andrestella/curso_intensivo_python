age = 40

if age < 2:
    estagio = 'bebê'
elif age < 4:
    estagio = 'criança'
elif age < 13:
    estagio = 'garoto'
elif age < 20:
    estagio = 'adolescente'
elif age < 65:
    estagio = 'adulto'
elif age >= 65:
    estagio = 'idoso'

print("A pessoa encontra-se no estágio: {}.".format(estagio))