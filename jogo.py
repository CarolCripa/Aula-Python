import random

print("Bem-Vindo ao Advinhe o Número!")
print("As regras são simples, vou pensar em um número e você tentará advinhá-lo.")

numero = random.randint(1, 10)
isGuessRight = False
while isGuessRight != True:
    advinha = input("Digite um número de 1 a 10: ")
    if int(advinha) == numero:
        print("Você digitou {}. O número está correto! Você Ganhou!".format(advinha))
        isGuessRight = True
    else:
        print("Você digitou {}. Desculpe, não é isso. Tente novamente!".format(advinha))
