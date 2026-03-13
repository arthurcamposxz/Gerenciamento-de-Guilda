from aventureiros.aventureiros import cadastrar_heroi, ver_herois
from missoes.missoes import enviar_missao
from utilidades.utilidades import somar_tesouro

guilda = []

while True:
    print("\n===== GUILDA DE AVENTUREIROS =====")
    print("1 - Cadastrar novo herói")
    print("2 - Ver heróis")
    print("3 - Enviar herói para missão")
    print("4 - Abrir Baú Mágico")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        heroi = cadastrar_heroi()
        guilda.append(heroi)

    elif opcao == "2":
        ver_herois(guilda)

    elif opcao == "3":
        if len(guilda) == 0:
            print("Nenhum herói cadastrado.")
            continue

        ver_herois(guilda)
        i = int(input("Escolha o número do herói: "))

        if i < 0 or i >= len(guilda):
            print("Herói inválido.")
            continue

        enviar_missao(guilda[i])

    elif opcao == "4":
        bau = [50, 100, [20, 30, [5, 10]]]
        total = somar_tesouro(bau)
        print(f"O baú tinha {total} moedas de ouro!")

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
