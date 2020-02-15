prompt = "Informe sua idade."
prompt += "\n(Para sair digite 'quit'): "

while True:
    idade = input(prompt)
    if idade == 'quit':
        break
    elif int(idade) <= 3:
        preco = 0
    elif int(idade) <= 12:
        preco = 10
    elif int(idade) > 12:
        preco = 15
    print("O ingresso custa {} dólares.".format(preco))