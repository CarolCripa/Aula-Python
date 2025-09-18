'''userReply = input("Você precisa enviar um pacote? (Digite Sim ou Não) ")
if userReply == "Sim":
    print("Podemos ajudá-lo a enviar o pacote!")

else:
    print("Volte quando precisar enviar um pacote. Obrigada.")'''

usuario = input("Você deseja comprar selos, comprar envelopes ou tirar uja cópia? (Digite: Selo, Envelope, Cópia)")
if usuario == "Selo":
    print("Temos muitos designes para escolher.")
elif usuario == "Envelopes":
    print("Temos vários tamanhos de envelopes para escolher.")
elif usuario == "Cópia":
    copias = input("Quatas cópias deseja fazer? (Digite o número de cópias)")
    print("Aqui está {} cópias".format(copias))
else:
    print("Obrigada!Volte outra hora")