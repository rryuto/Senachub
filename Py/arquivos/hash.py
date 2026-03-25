#Hash
#o que é hash? é uma transformação de senha
#senha > hash(irreversivel)
#ex: 123 vira "a665a45920422f9d..." é feito para que se o arquivo json for roubado as senhas estão incriptiografadas. 

#2. Biblioteca profissional bcrypt
#instalar # import bcrypt

# senha = "123".encode()  # precisa virar bytes

# hash_senha = bcrypt.hashpw(senha, bcrypt.gensalt())

# print(hash_senha)

import bcrypt

senha ="123".encode() #precisa virar bytes
hash_senha = bcrypt.hashpw(senha, bcrypt.gensalt())
print(hash_senha)

senha_digitada = "123".encode()

if bcrypt.checkpw(senha_digitada, hash_senha):
    print("Senha correta!")
else:
    print("Senha incorreta!")