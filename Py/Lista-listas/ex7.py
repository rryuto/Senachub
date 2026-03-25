numeros = [10, 5, 22, 8, 31, 4]
pares = []
impares = []

for numero in numeros:
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)
