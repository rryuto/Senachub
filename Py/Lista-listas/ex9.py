poltronas = ["Livre", "Livre", "Livre", "Livre", "Livre"]
saida = 0
check = 0
while saida != 9 and check != 5:

  for i, poltrona in enumerate(poltronas):
    print(f"Poltrona {i} - {poltrona}\n")
  print(f"Sair - digite 9:")

  reserva = int(input(f"Qual poltrona deseja reservar? \n"))
  if reserva == 9:
    break

  if poltronas[reserva] == "Livre":
    poltronas[reserva] = "Ocupado"
    check += 1
  else:
    print("Poltrona ja está ocupada.\n")

