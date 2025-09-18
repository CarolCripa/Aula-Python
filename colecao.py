#Lista
listaFrutas = ["Banana", "uva", "manga"]
print("Minha lista de frutas original: ", listaFrutas)
print(type(listaFrutas))

print(listaFrutas[0])
print(listaFrutas[1])
print(listaFrutas[2])

listaFrutas[0] = "Abacaxi"
print("Minha lista de frutas alterada: ",listaFrutas)


#Tupla
tuplaFrutas = ("limão", "morango", "maracujá")
print("A minha TUPLA de frutas é: ",tuplaFrutas)
print(type(tuplaFrutas))

print(tuplaFrutas[0])
print(tuplaFrutas[1])
print(tuplaFrutas[2])


#Dicionário
dicioFrutas = {
    "Ricardo": "Limão",
    "Gustavo": "Uva",
    "Taciara": "Tangerina",
    "Carol": "Manga",
}

print("Meu dicionário de frutas e pessoas favoritas é ",dicioFrutas)
print(type(dicioFrutas))
print("A Carol gosta de ",dicioFrutas["Carol"])
print("O Gustavo gosta de ",dicioFrutas["Gustavo"])
print("O Ricardo gosta de ",dicioFrutas["Ricardo"])
print("A Taciára gosta de ",dicioFrutas["Taciara"])
