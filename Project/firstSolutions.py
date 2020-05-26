# valores = [conjA, conjB, intersec, vfora, total]

def ConjuntoA(valores):
    cA = valores[0]
    if cA == 0:
        cA = valores[4] - (valores[1] + valores[2] + valores[3])
        return cA
    else:
        cA -= valores[2]
        return cA
    return valores


def ConjuntoB(valores):
    cB = valores[1]
    if cB == 0:
        cB = valores[4] - (valores[0] + valores[2] + valores[3])
        return cB
    else:
        cB -= valores[2]
        return cB
    return valores


def Intersec(valores):
    solution = valores[0] + valores[1] + valores[3]
    solution -= valores[4]
    valores[2] = solution
    return solution


def conjInter(valores):
    value = (valores[0] - valores[2]) + (valores[1] - valores[2]) + valores[2]
    return value

def ValueNotIn(valores):
    solution = (conjInter(valores) - valores[4])*(-1)
    valores[3] = solution
    return solution


def ValorTotal(valores):
    solution = conjInter(valores) + valores[3]
    valores[4] = solution
    return solution

