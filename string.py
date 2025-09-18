myString = "Isso é uma String"

print(myString)
print(type(myString))
print(myString + " é do tipo de dado " + str(type(myString)))

fristString = "water"
secondString = "fall"
thirdString = fristString + secondString
print(thirdString)

name = input("Qual é o seu nome? ")
color = input("Qual a sua cor favorita? ")
animal = input("Qual seu animal favorito? ")
print("{}, você gosta da cor {} e do animal {}!".format(name, color, animal))