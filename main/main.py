from time import sleep

print("DIAGRAMA DE VENN ")
sleep(0.3)

notnumeric = 2
while notnumeric > 1:
    valores = [input("\nConjunto A: "),  # conjunto A
               input("Conjunto B: "),  # conjunto B
               input("Intersecção A e B: "),  # intersecção
               input("Valor de fora: "),  # valor fora do conjunto A e conjunto B
               input("Conjunto Universo: ")  # conjunto total
               ]
    sleep(0.5)
    notnumeric = 0
    for value in valores:
        if value.isnumeric():
            value = valores.index(value)
            valores[value] = int(valores[value])
        else:
            pos = valores.index(value)
            notnumeric += 1
    if notnumeric > 1:
        print("Por favor, somente uma variável. Reavalie seus valores.")
        sleep(0.5)
