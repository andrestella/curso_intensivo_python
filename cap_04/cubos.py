cubos = []
for value in range(1,11):
    cubos.append(value**3)
for cubo in cubos:
    print(cubo)

cubos = [value**3 for value in range(1,11)]
for cubo in cubos:
    print(cubo)