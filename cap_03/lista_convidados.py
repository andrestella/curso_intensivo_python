lista_convidados = []
lista_convidados.append('andré')
lista_convidados.append('maria')
lista_convidados.append('henri')
lista_convidados.append('nádia')
print(lista_convidados)
print("Olá {} ! Vamos jantar em casa hoje?".format(lista_convidados[0].title()))
print("Olá {} ! Vamos jantar em casa hoje?".format(lista_convidados[1].title()))
print("Olá {} ! Vamos jantar em casa hoje?".format(lista_convidados[2].title()))
print("Olá {} ! Vamos jantar em casa hoje?".format(lista_convidados[3].title()))

nao_comparecer = lista_convidados.pop(0)
print("\n" + str(lista_convidados))
print("Infelizmente o {} não comparecerá ao jantar.".format(nao_comparecer.title()))

lista_convidados.insert(0, 'nayla')
print("\n" + str(lista_convidados))
print("Olá {} ! Vamos jantar em casa hoje?".format(lista_convidados[0].title()))
print("Olá {} ! Vamos jantar em casa hoje?".format(lista_convidados[1].title()))
print("Olá {} ! Vamos jantar em casa hoje?".format(lista_convidados[2].title()))
print("Olá {} ! Vamos jantar em casa hoje?".format(lista_convidados[3].title()))

lista_convidados.insert(0, 'andré')
lista_convidados.insert(2, 'ana')
lista_convidados.append('tereza')
print("\n" + str(lista_convidados))
print("Encontrei uma mesa de jantar maior!")
print("Olá {} ! Vamos jantar hoje?".format(lista_convidados[0].title()))
print("Olá {} ! Vamos jantar hoje?".format(lista_convidados[1].title()))
print("Olá {} ! Vamos jantar hoje?".format(lista_convidados[2].title()))
print("Olá {} ! Vamos jantar hoje?".format(lista_convidados[3].title()))
print("Olá {} ! Vamos jantar hoje?".format(lista_convidados[4].title()))
print("Olá {} ! Vamos jantar hoje?".format(lista_convidados[5].title()))
print("Olá {} ! Vamos jantar hoje?".format(lista_convidados[6].title()))

print("\nHouve um contratempo e poderei convidar apenas duas pessoas para o jantar.")
removido = lista_convidados.pop()
print("{}, sinto muito por não convidá-lo para o jantar.".format(removido.title()))
removido = lista_convidados.pop()
print("{}, sinto muito por não convidá-lo para o jantar.".format(removido.title()))
removido = lista_convidados.pop()
print("{}, sinto muito por não convidá-lo para o jantar.".format(removido.title()))
removido = lista_convidados.pop()
print("{}, sinto muito por não convidá-lo para o jantar.".format(removido.title()))
removido = lista_convidados.pop()
print("{}, sinto muito por não convidá-lo para o jantar.".format(removido.title()))
print("Olá {}! Vamos jantar hoje?".format(lista_convidados[0].title()))
print("Olá {}! Vamos jantar hoje?".format(lista_convidados[1].title()))
print("Estou convidando {} pessoas para o jantar.".format(len(lista_convidados)))
print(lista_convidados)
del lista_convidados[0]
print(lista_convidados)
del lista_convidados[0]
print(lista_convidados)