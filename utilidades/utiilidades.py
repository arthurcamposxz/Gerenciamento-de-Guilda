def somar_tesouro(bau):
    total = 0

    for item in bau:
        if type(item) == int:
            total += item

        elif type(item) == list:
            total += somar_tesouro(item)

    return total
