current_users = ['andré', 'henri', 'nádia', 'Maria', 'nayla']
new_users = ['André', 'HENRI', 'alexandre', 'stella', 'ana', 'tereza', 'maria']

# current_users_lower = []
# for user in current_users:
#     current_users_lower.append(user.lower())

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("O nome escolhido ({}) já está sendo utilizado. Escolha outro nome.".format(new_user))
    else:
        print("O nome escolhido ({}) está disponível".format(new_user))