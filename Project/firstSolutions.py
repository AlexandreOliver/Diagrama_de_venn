
def ConjuntoA(valores):
    return valores


def ConjuntoB(valores):
    return valores


def Intersec(v):
    soma = v[0] + v[1] + v[3]
    solution = soma - v[4]
    return solution


def conjInter(v):
    volta = (v[0] - v[2]) + (v[1] - v[2]) + v[2]
    return volta


def ValueNotIn(v):
    solution = conjInter(v)
    solution = (solution - v[4])*(-1)
    return solution


def ValorTotal(v):
    solution = conjInter(v)
    solution += v[3]
    return solution

