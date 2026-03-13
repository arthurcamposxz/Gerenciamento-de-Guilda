def cadastrar_heroi():
    nome = input("Nome do herói: ")
    classe = input("Classe (Guerreiro, Mago, Arqueiro): ")
    nivel = int(input("Nível inicial: "))
    vida = float(input("Vida inicial: "))

    inventario = []
    while True:
        item = input("Adicionar item ao inventário (ou 'sair'): ")
        if item.lower() == "sair":
            break
        inventario.append(item)

    heroi = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel,
        "vida": vida,
        "inventario": inventario
    }

    print("Herói cadastrado com sucesso!")
    return heroi


def ver_herois(guilda):
    if len(guilda) == 0:
        print("Nenhum herói na guilda.")
        return

    for i, h in enumerate(guilda):
        print(f"\n[{i}] {h['nome']}")
        print(f"Classe: {h['classe']}")
        print(f"Nível: {h['nivel']}")
        print(f"Vida: {h['vida']}")
        print(f"Inventário: {h['inventario']}")
