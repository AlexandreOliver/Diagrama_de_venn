from connection import options, resp
from time import sleep
import os, platform, sys

op = False
if platform.system() == 'Windows':
    op = True

def clear():
    if op:
        return os.system('cls')
    return os.system('clear')


def program1():
    global valores, allsolutions
    print("Adicione zero(0) ao valor que você não possui.")
    valores = [input("Conjunto A: "),
                input("Conjunto B: "),
                input("Intersecção: "),
                input("Valor fora dos conjuntos: "),
                input("Total: ")]    # Conjunto U
    allsolutions = (
        "Conjunto A --",
        "Conjunto B --",
        "Intersecção --",
        "Conjunto Fora --",
        "Conjunto U --")

    sleep(1)
    for value in valores:
        if value.isnumeric():
            posValue = valores.index(value)
            valores[posValue] = int(valores[posValue])
        else:
            clear()
            print("Utilize apenas Numeros!!\n Tente Novamente.\n")
            sleep(0.4)
            return program1()
    clear()


def execut():
    global user, resultado
    print("\n", "<"*4, "O que vc deseja que o Programa faça?", ">"*4)
    print("         Para sair digite 'exit' :D")
    print("N°", " "*15, "Opções")
    for n, opcao in options.items():
        print(n, " "*2, opcao, "|")
    print("<"*7, "Digite o Numero Correspondente:", ">"*6)
    user = str(input("===> ")).strip().lower()
    if user == 'exit':
        bye()
    resultado = resp(user, valores)


def bye():
    sleep(0.3)
    clear()
    print("Volte logo :D\n"
          "Contribuidores:\n"
          "Alexandre Oliver\n"
          "Richard Smanhoto")
    exit()


clear()
print("-=" * 23)
print("   PROGRAMA DE RESOLUÇÃO DO DIAGRAMA DE VENN")
print("-=" * 23, "\n")
program1()
while True:
    clear()
    execut()
    if resultado == None:
        print('Value Error. Digite novamente.')
    else:
        print(f'Resultado encontrado: {resultado}')
        for k in allsolutions:
            p = allsolutions.index(k)
            print(f"{k} {valores[p]}")
    input()
