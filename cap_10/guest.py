arquivo = "guest.txt"

with open(arquivo, 'w') as arquivo_obj:
    nome = input("Qual seu nome? ")
    arquivo_obj.write(nome)

with open(arquivo) as arquivo_obj:
    conteudo = arquivo_obj.read()
    print(conteudo)