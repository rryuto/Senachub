#funções

def saudacao():
    print("Olá!")

saudacao()
#funcao com parametro
def saudacao(nome):
    print(f"Olá {nome}!")

saudacao("Rodrigo")

#funcao com retorno
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)

