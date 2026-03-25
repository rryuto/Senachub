#lista criada
usuarios = [
    {"nome": "joao", "senha": "123"},
    {"nome": "maria", "senha": "abc"}
]
#importando json
import json
#Salvando a lista em json como arquivo
with open("usuario.json", "w") as arquivo:
    json.dump(usuarios, arquivo)