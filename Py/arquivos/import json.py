#importando json
import json
#abrindo para ler a lista de arquivos de json
with open("usuarios.json", "r") as arquivo:
    usuarios = json.load(arquivo)
#imprimindo a lista criada em outro programa
print(usuarios)

#evitando erro na primeira execução se arquivo ainda não existir

import json

try:
    with open("usuarios.json", "r") as arquivo:
        usuarios = json.load(arquivo)

except:
    usuarios = []