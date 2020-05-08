from firstSolutions import ConjuntoA, ConjuntoB, Intersec, ValueNotIn,ValorTotal


options = {1: "Descobrir valor do Conjunto A      ",
           2: "Descobrir valor do Conjunto B      ",
           3: "Descobrir valor da Intersecção AB  ",
           4: "Descobrir valor Fora dos Conjuntos ",
           5: "Descobrir valor total              "}


def resp(user, valores):
    if user == "1":
        return ConjuntoA(valores)
    elif user == "2":
        return ConjuntoB(valores)
    elif user == "3":
        return Intersec(valores)
    elif user == "4":
        return ValueNotIn(valores)
    elif user == "5":
        return ValorTotal(valores)
    else:
        return
