
def ConjuntoA(valores):
    return valores


def ConjuntoB(valores):
    return valores


def Intersec(valores):
    value = valores
    soma = value[0] + value[1] + value[3]
    solution = soma - value[4]
    return solution


def ValueNotIn(valores):
    value = valores
    solution = (value[0] - value[2]) + (value[1] - value[2]) + value[2]
    solution = (solution - value[4])*(-1)
    return solution


def ValorTotal(valores):
    value = valores

    return value

