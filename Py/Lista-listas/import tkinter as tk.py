import tkinter as tk
import sqlite3
import bcrypt

# função de login
def login():
    nome = entry_nome.get()
    senha = entry_senha.get().encode()

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("SELECT senha FROM usuarios WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()

    if resultado:
        hash_guardado = resultado[0].encode()

        if bcrypt.checkpw(senha, hash_guardado):
            label_resultado.config(text="Bem-vindo!")
        else:
            label_resultado.config(text="Senha incorreta.")
    else:
        label_resultado.config(text="Usuário não encontrado.")

    conn.close()

# janela
janela = tk.Tk()
janela.title("Sistema de Login")

# campos
tk.Label(janela, text="Usuário").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Senha").pack()
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

# botão
tk.Button(janela, text="Login", command=login).pack()

# resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()