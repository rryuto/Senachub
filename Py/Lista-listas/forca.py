palavra = "python"
letras_descobertas = ["_"] * len(palavra)
tentativas = 6

print("=== JOGO DA FORCA ===")

while tentativas > 0 and "_" in letras_descobertas:

    print("\nPalavra:", " ".join(letras_descobertas))
    letra = input("Digite uma letra: ")

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                letras_descobertas[i] = letra
    else:
        tentativas -= 1
        print("Letra errada! Tentativas restantes:", tentativas)

if "_" not in letras_descobertas:
    print("\nParabéns! Você acertou a palavra:", palavra)
else:
    print("\nVocê perdeu! A palavra era:", palavra)