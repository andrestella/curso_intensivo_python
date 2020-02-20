arquivo = "polling.txt"

with open(arquivo, 'w') as arquivo_obj:
    while True:
        sondagem = input("Fale um motivo para gostar de programação: ")
        if sondagem == 'sair':
            break
        arquivo_obj.write(sondagem + "\n")

with open(arquivo) as arquivo_obj:
    conteudo = arquivo_obj.read()
    print(conteudo)