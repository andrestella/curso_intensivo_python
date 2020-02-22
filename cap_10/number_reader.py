import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    # numbers = f_obj.read()

print(numbers)