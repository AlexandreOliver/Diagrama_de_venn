from time import sleep
from connection import options, resp

print("-=" * 21)
print("PROGRAMA DE RESOLUÇÃO DO DIAGRAMA DE VENN")
print("-=" * 21)

num = 5
while num > 0:
    print("Adicione zero(0) ao valor que você não possui.")
    valores = [input("Conjunto A: "),
               input("Conjunto B: "),
               input("Intersecção: "),
               input("Valor fora dos conjuntos: "),
               input("Total: ")]    # Conjunto U
    sleep(1)
    for value in valores:
        if value.isnumeric():
            value = valores.index(value)
            valores[value] = int(valores[value])
            num -= 1
        else:
            print("\nUtilize apenas Numeros!!\n Tente Novamente.\n")
            sleep(0.5)

print("\n")
print("<"*4, "O que vc deseja que o Programa faça?", ">"*4)
print("N°", " "*15, "Opções")
for n, opcao in options.items():
    print(n, " "*2, opcao, "|")
print("<"*7, "Digite o Numero Correspondente:", ">"*6)
user = input("===> ")
resp(user)