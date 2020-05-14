
def ConjuntoA(valores):
    return valores


def ConjuntoB(valores):
    return valores


def Intersec(valores):
    v = valores
    soma = v[0] + v[1] + v[3]
    solution = soma - v[4]
    return solution


def conjInter(valores):
    v = valores
    volta = (v[0] - v[2]) + (v[1] - v[2]) + v[2]
    return volta


def ValueNotIn(valores):
    v = valores
    solution = conjInter(v)
    solution = (solution - v[4])*(-1)
    return solution


def ValorTotal(valores):
    v = valores
    solution = conjInter(v)
    solution += v[3]
    return solution

