prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.): "

while True: # um laço que comece com "while True:" executará indefinidamente,
# a menos que alcance uma instrução "break"
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to {}!".format(city.title()))