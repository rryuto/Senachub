#calculadora simples

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

a = int(input("Numero A"))
b = int(input("Numero B"))
print(f"Qual função deseja fazer?")
print(f"1.Somar")
print(f"2.Subtrair")
print(f"3.Multiplicar")
print(f"4.Dividir")
print(f"5.Sair")
opcao = 0

while opcao != 5:
    opcao = int(input())
    if opcao == 1:
        print(somar(a,b))
    elif opcao == 2:
        print(subtrair(a,b))
    elif opcao == 3:
        print(multiplicar(a,b))
    elif opcao == 4:
        print(dividir(a, b))
    elif opcao == 5:
        break
