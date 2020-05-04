from firstSolutions import ConjuntoA,ConjuntoB,Interseccao,ValueNotIn,ValorTotal


options = {1: "Descobrir valor do Conjunto A      ",
           2: "Descobrir valor do Conjunto B      ",
           3: "Descobrir valor da Intersecção AB  ",
           4: "Descobrir valor de Fora            ",
           5: "Descobrir valor total              "}


def resp(user, valores):
    if user == "1":
        print("1")  # calculo 1
    elif user == "2":
        print("2")  # calculo 2
    elif user == "3":
        print("3")  # calculo 3
    elif user == "4":
        print("4")  # calculo 4
