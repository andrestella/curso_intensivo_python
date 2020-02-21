print("Calculadora para adição. Digite 'q' para sair.")

while True:
    print("\nInforme dois números para eu fornecer a soma dos mesmos.")
    try:
        first_number = input("Primeiro número: ")
        if first_number == 'q':
            break
        first_number = int(first_number)
        second_number = input("Segundo número: ")
        if second_number == 'q':
            break
        second_number = int(second_number)
    except ValueError:
        print("Informe apenas números!")    
    else:
        sum_numbers = first_number + second_number
        print("A soma de {} com {} resulta em {}."
            .format(first_number, second_number, sum_numbers))