items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)


def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # la inserción empieza desde el segundo elemento
    j = None


def step():
    global items, n, i, j

    # Si ya terminamos todo el arreglo
    if i >= n:
        return {"a": None, "b": None, "swap": False, "done": True}

    # Si j es None, recién empezamos a trabajar con items[i]
    if j is None:
        j = i
        # No hacemos swap todavía, solo marcamos qué dos elementos miramos
        return {"a": j-1, "b": j, "swap": False, "done": False}

    # Si podemos hacer un swap (desplazar hacia la izquierda)
    if j > 0 and items[j - 1] > items[j]:
        # swap
        items[j - 1], items[j] = items[j], items[j - 1]
        j -= 1
        return {"a": j, "b": j+1, "swap": True, "done": False}

    # Si ya no hay que desplazar más, avanzamos i
    i += 1
    j = None
    return {"a": None, "b": None, "swap": False, "done": False}
