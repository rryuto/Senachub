#jogodaforca

import random
numero = random.randint(0, 2)

lista_palavras = ["banana", "farofa", "elefante"]

palavra = lista_palavras[numero]
print(palavra)
check = 0

while True:
    print("\n-- Jogo da forca --\n")
    letra = input("digite uma letra:")
    for i in palavra:
        if letra == i:
            check += 1
    

    if check == len(palavra):
        print("Parabéns vc acertou!")
        break