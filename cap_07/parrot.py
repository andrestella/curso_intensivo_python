prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\n(Enter 'quit' to end the program): "

# Usando uma flag (muitos eventos diferentes poderiam fazer o programa parar):
active = True # flag de nome "active": controlará se o programa deve ou não continuar executando
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)