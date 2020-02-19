filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = '040579'
if birthday in pi_string:
    print("Sua data de nascimento aparece no primeiro milhão de dígitos de 'pi'.")
else:
    print("Sua data de nascimento não aparece no primeiro milhão de dígitos de 'pi'.")