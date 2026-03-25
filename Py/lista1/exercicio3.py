#distancia
#consumo
#preco

distancia = int(input("Qual a distância da viagem?(em KM) "))
consumo = int(input("Qual o consumo por litro do seu carro?(KM/L) "))
preco = float(input("Qual o preço da gasolina? "))
gastototal = distancia/consumo

print(f"Seu carro consumira {gastototal} Litros de gasolina")
print(f"Sua viagem custara {gastototal*preco}R$")