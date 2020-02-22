import json

numero_favorito = int(input("Qual seu número favorito? "))

filename = 'numero_favorito.json'

with open(filename, 'w') as f_obj:
    json.dump(numero_favorito, f_obj)