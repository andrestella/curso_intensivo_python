# from user2 import User
from admin3 import Admin

administrador = Admin('andré', 'alexandre', 40)
administrador.describe_user()
administrador.privileges.privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]
administrador.privileges.show_privileges()