my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # copiando uma lista

print(id(my_foods))
print(id(friend_foods))

# Isto não funciona como cópia de uma lista:
# friend_foods = my_foods
# print(id(my_foods))
# print(id(friend_foods))

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for food in my_foods:
    print("- " + food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print("- " + food)