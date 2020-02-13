# Aqui dividimos um dicionário em várias linhas:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', # incluir uma vírgula após o último par
    # chave-valor é uma boa prática; assim você estará preparado para
    # acrescentar um novo par chave-valor na próxima linha.
    }

# Como dividir uma instrução "print()" longa em várias linhas:
# - operador de concatenação (+)
# - alinhar com um nível de indentação
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".\n")
# - utilizando a instrução print() em mais de uma linha com a função format():
# print("Sarah's favorite language is {}.\n"
#     .format(favorite_languages['sarah'].title()))

# O método "items()" devolve uma lista de pares chave-valor
print(favorite_languages.items())
for name, language in favorite_languages.items():
    print("{}'s favorite language is {}."
        .format(name.title(), language.title()))

print("\n")

# O método "keys()" extrai todas as chaves do dicionário
print(favorite_languages.keys())
for name in favorite_languages.keys():
    print(name.title())
# Percorrer as chaves, na verdade, é o comportamento-padrão quando
# percorremos um dicionário com um laço, portanto o código abaixo 
# produzirá o mesmo resultado que o código acima:
for name in favorite_languages:
    print(name.title())
# O método "keys()" pode ser usado explicitamente se isso deixar o
# código mais fácil de ler, ou podemos omití-lo, se quisermos

print("\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("\tHi {}, I see your favorite language is {}!"
        .format(name.title(), favorite_languages[name].title()))

print("\n")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!\n")

# Percorrendo as chaves de um dicionário em ordem com a função "sorted()":
for name in sorted(favorite_languages.keys()):
    print("{}, thank you for taking the poll.".format(name.title()))

print("\n")

# O método "values()" extrai todos os valores do dicionário
# - essa abordagem extrai todos os valores, sem verificar se há repetições
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# Para ver cada valor sem repetições, podemos usar um conjunto (set)
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())