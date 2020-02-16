# Usando argumentos nomeados arbitrários
def build_profile(first, last, **user_info): # os asteriscos duplos (**)  
# fazem Python criar um dicionário vazio e colocar quaisquer pares 
# nome-valor recebidos nesse dicionário
    """ Constrói um dicionário contendo tudo que sabemos sobre um usuário. """
    profile = {}
    profile['fisrt_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

def show_profile(user_profile):
    """ Exibe os dados do usuário de forma elegantes. """
    for key, value in user_profile.items():
        print("- {}: {}".format(key, value))

def show_profiles(profiles):
    """ Exibe os dados de todos os usuário de forma elegantes. """
    for profile in profiles:
        show_profile(profile)
        print("\n")

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
user_profile2 = build_profile('andré', 'stella',
                            age=40,
                            location='são paulo',
                            field='computação')
user_profile3 = build_profile('henri', 'stella')


profiles = [user_profile, user_profile2, user_profile3]

show_profiles(profiles)