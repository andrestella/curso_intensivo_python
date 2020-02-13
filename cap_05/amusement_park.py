age = 40

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

# Quando usar "if-elif-else" e quando usar uma série de instruções "if"?
# Se quiser que apenas um bloco de código seja executado, utilize uma
# cadeia "if-elif-else". Se mais de um bloco de código deve executar,
# utilize uma série de instruções "if" independentes.

# Omitindo o bloco "else":
# O bloco "else" é uma instrução que captura tudo. Ela corresponde a 
# qualquer condição não atendida por um teste "if" ou "elif" específicos,
# e isso, às vezes, pode incluir dados inválidos ou até mesmo maliciosos.
# Se você tiver uma condição final para testar, considere usar um último
# bloco "elif" e omitir o bloco "else". Como resultado, você terá mais
# confiança de que seu código executará somente nas condições corretas.

# else:
    # price = 5

print("Your admission cost is ${}.".format(price))