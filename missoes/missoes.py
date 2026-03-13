import random

def bonus_classe(classe):
    if classe.lower() == "guerreiro":
        return 2
    elif classe.lower() == "mago":
        return 1
    elif classe.lower() == "arqueiro":
        return 1
    else:
        return 0


def enviar_missao(heroi):
    dificuldade = random.randint(1, 10)

    print(f"\nMissão com dificuldade {dificuldade}")

    poder = heroi["nivel"] + bonus_classe(heroi["classe"])

    if poder > dificuldade:
        heroi["nivel"] += 1
        print(f"{heroi['nome']} venceu a missão!")
        print("Subiu de nível!")
        return True

    else:
        heroi["vida"] -= 10
        print(f"{heroi['nome']} perdeu a missão.")
        print("Perdeu 10 de vida.")
        return False    
