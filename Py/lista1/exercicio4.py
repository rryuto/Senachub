#velocidade do carro > se acima da velocidade > cora 7R$ a cada km/h acima da velocidade

velocidade = int(input("Velocidade do carro: "))
velocidade_ultrapassada = 0
if velocidade > 80:
    velocidade_ultrapassada = velocidade - 80
    print(f"Você ultrapassou o limite de velocidade e sua multa será {velocidade_ultrapassada*7}R$")
else:
    print(f"Sua velocidade é {velocidade} e está dentro do limite da via. Boa viagem!")