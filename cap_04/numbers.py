# A função "range()" facilita gerar uma série de números
for value in range(1,5):
    print(value)

# Usando "range()" para criar uma lista de números com a função "list()"
numbers = list(range(1,5))
print(numbers)

# Listar os números pares entre 1 e 10
even_numbers = list(range(2,11,2))
print(even_numbers)

# Listar os números ímpares entre 1 e 10
odd_numbers = list(range(1,11,2))
print(odd_numbers)

# Estatísticas simples com uma lista de números
digits = list(range(0,10))
print(digits)
print(min(digits)) # valor mínimo
print(max(digits)) # valor máximo
print(sum(digits)) # soma

# Listar os 10 primeiros quadrados perfeitos
squares = []
for value in range(1,11):
    # square = value**2
    # squares.append(square)
    squares.append(value**2)
print(squares)

# Listar os 10 primeiros quadrados perfeitos usando uma 'list comprehension'
squares = [value**2 for value in range(1,11)]
print(squares)