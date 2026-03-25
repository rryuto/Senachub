import random
numero_secreto = random.randint(1, 10)

while True:
    numero = int(input("Adivinhe o número secreto(1 a 10): "))
    if numero == numero_secreto:
        print("Acertou miserável!")
        break
    else:
        print("Errrouu! Tente denovo!")