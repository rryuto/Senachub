cupons = {
    "DESC10": 10,
    "DESC20": 20,
    "DESC30": 30,
    "DESC40": 40
}
# cupom_valido = None
codigo = input("Digite um código de cupom: ")

# for chave, valor in cupons.items():
#     if codigo == chave:
#         cupom_valido = True

# if cupom_valido == True:

if codigo in cupons:
    print("Cupom válido!")
else:
    print("Cupom inexistente.")
