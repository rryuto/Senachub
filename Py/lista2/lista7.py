i = 0
soma = 0

while True:
    numero = int(input(f"Digite o números: "))
    if numero == 0:
        break    
    soma += numero 
    i += 1
print(f"A quantidade dos números é: {i}")
print(f"A soma dos números é igual a: {soma}")
