
def ConjuntoA(valores):
    return valores


def ConjuntoB(valores):
    return valores


def Intersec(valores):
    solution = valores[0] + valores[1] + valores[3]
    solution -= valores[4]
    valores[2] = solution
    return solution


def conjInter(list):
    value = (list[0] - list[2]) + (list[1] - list[2]) + list[2]
    return value

def ValueNotIn(valores):
    solution = (conjInter(valores) - valores[4])*(-1)
    valores[3] = solution
    return solution


def ValorTotal(valores):
    solution = conjInter(valores) + valores[3]
    valores[4] = solution
    return solution

