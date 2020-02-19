import codecs

arquivo = "aprendendo_python.txt"

with open(arquivo, encoding="utf-8") as arquivo_obj:
    linhas = arquivo_obj.readlines()

for linha in linhas:
    linha = linha.replace('Python', 'C')
    # O método 'replace()' substitui qualquer palavra por uma palavra 
    # diferente em uma string.
    print(linha.rstrip())