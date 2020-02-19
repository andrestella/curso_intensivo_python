import codecs

arquivo = "aprendendo_python.txt"

with open(arquivo, encoding='utf-8') as arquivo_obj:
    conteudo = arquivo_obj.read()
    print(conteudo.rstrip())

with open(arquivo, encoding='utf-8') as arquivo_obj:
    for linha in arquivo_obj:
        print(linha.rstrip())

with open(arquivo, encoding='utf-8') as arquivo_obj:
    linhas = arquivo_obj.readlines()
for linha in linhas:
    print(linha.rstrip())