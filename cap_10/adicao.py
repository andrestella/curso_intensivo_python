print("Informe dois números para eu fornecer a soma dos mesmos.")
try:
    first_number = int(input("Primeiro número: "))
    second_number = int(input("Segundo número: "))
except ValueError:
    print("Informe apenas números!")    
else:
    sum_numbers = first_number + second_number
    print("A soma de {} com {} resulta em {}."
        .format(first_number, second_number, sum_numbers))