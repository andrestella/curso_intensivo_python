arquivo = "guest_book.txt"

with open(arquivo, 'w') as arquivo_obj:
    while True:
        name = input("Qual seu nome: ")
        if name == 'sair':
            break
        print("Olá {}, seja bem vindo!".format(name))
        arquivo_obj.write(name + "\n")

with open(arquivo) as arquivo_obj:
    conteudo = arquivo_obj.read()
    print(conteudo)