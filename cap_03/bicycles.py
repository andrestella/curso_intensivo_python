bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-4])

message = "My first bicycle was a " + bicycles[0].title() + "."
message2 = "My first bicycle was a {}.".format(bicycles[0].title())
print(message)
print(message2)