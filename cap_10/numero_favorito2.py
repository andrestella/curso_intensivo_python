import json

filename = 'numero_favorito.json'

with open(filename) as f_obj:
    numero_favorito = json.load(f_obj)

print("Eu sei qual é o seu número favorito! É {}.".format(numero_favorito))