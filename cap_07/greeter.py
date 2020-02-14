name = input("Please enter your name: ")
print("Hello, {}!\n".format(name))

#Escrevendo um prompt com mais de uma linha:
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, {}!".format(name))