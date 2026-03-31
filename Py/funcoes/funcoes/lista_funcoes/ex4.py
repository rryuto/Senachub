def conversao(valor, taxa):
    return valor * taxa

real = float(input(f"R$: "))
cambio = float(input(f"Valor do câmbio: "))
# total = conversao(real, cambio)

print(f"Total conversão: {conversao(real, cambio)}")