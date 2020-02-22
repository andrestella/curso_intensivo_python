import json

try:
    filename = 'numero_favorito2.json'
    with open(filename) as f_obj:
        numero_favorito = json.load(f_obj)
except FileNotFoundError:
    numero_favorito = int(input("Qual seu número favorito? "))
    with open(filename, 'w') as f_obj:
        json.dump(numero_favorito, f_obj)
else:
    print("Eu sei qual é o seu número favorito! É {}.".format(numero_favorito))