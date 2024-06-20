import random

def move_name(mov):
    if mov == 1:
        move = "piedra"
    elif mov == 2:
        move = "papel"
    elif mov == 3:
        move = "tijera"

    return move

print("      JUEGO DE PIEDRA PAPEL O TIJERAS      ")
mov_player = int(input("Digite su jugada \n 1. piedra \n 2. papel \n 3. tijera \n"))

mov_bot = random.randint(1 , 3)

name_mov_player = move_name(mov_player)
name_mov_bot = move_name(mov_bot)

print(f"El jugador eligió {name_mov_player} y la máquina eligió {name_mov_bot}")

if mov_bot == mov_player:
    print("Empate")

elif (mov_bot == 1 or mov_player == 1) and (mov_bot == 2 or mov_player == 2):
    print("Gana papel")

elif (mov_bot == 1 or mov_player == 1) and (mov_bot == 3 or mov_player == 3):
    print("Gana piedra")

elif (mov_bot == 2 or mov_player == 2) and (mov_bot == 3 or mov_player == 3):
    print("Gana tijera")


    