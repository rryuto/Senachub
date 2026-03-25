filmes = [
    {"titulo": "Avatar", "genero": "Fantasia"},
    {"titulo": "Vingadores", "genero": "Ação"},
    {"titulo": "IT", "genero": "Terror"}
]

busca = input("Digite o nome do filme: \n")

encontrado = False

for i in filmes:
    if i["titulo"] == busca:
        print(f"O filme {busca} esta no catálogo.")
        encontrado = True
        break

if not encontrado:
    print("Filme não esta no catálogo.")