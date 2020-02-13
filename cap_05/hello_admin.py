usuarios = ['admin', 'andré', 'henri', 'nádia', 'maria', 'nayla']
# usuarios = []

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print("Olá Administrador, gostaria de ver um relatório de status?")
        else:
            print("Olá {}, obrigado por fazer login novamente.".format(usuario.title()))
else:
    print("Precisamos encontrar alguns usuários!")