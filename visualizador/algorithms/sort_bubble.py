items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j

    # Si no quedan más pasadas → algoritmo terminado
    if i >= n - 1:
        return {"done": True}

    # Elegimos los índices a comparar
    a = j
    b = j + 1
    swap = False

    # Hacemos la comparación real
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    # Avanzamos j
    j += 1

    # Si ya llegamos al final de la pasada, avanzamos a la siguiente
    if j >= n - 1 - i:
        i += 1
        j = 0

    return {"a": a, "b": b, "swap": swap, "done": False}
