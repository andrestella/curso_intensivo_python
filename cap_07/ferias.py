ferias = {}

while True:
    pessoa = input("\nQual o seu nome? ('quit' para sair) ")
    if pessoa == 'quit':
        break
    lugar = input("Se pudesse visitar qualquer lugar do mundo, para onde você iria? ")
    ferias[pessoa] = lugar

for pessoa, lugar in ferias.items():
    print("\nAs férias dos sonhos de {} seriam em {}."
        .format(pessoa.title(), lugar.title()))