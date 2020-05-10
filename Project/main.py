from time import sleep
from connection import options, resp
from os import system
import platform


def sistema():
    if platform.system() == 'Windows':
        system('cls')
    elif platform.system() == 'Linux':
        system('clear')
    return


def program():
    global valores
    while True:
        inletra = False
        print("Adicione zero(0) ao valor que você não possui.")
        valores = [input("Conjunto A: "),
                   input("Conjunto B: "),
                   input("Intersecção: "),
                   input("Valor fora dos conjuntos: "),
                   input("Total: ")]    # Conjunto U
        sleep(1)
        for value in valores:
            if value.isnumeric():
                posValue = valores.index(value)
                valores[posValue] = int(valores[posValue])
            else:
                inletra = True
        if inletra:
            sistema()
            print("\nUtilize apenas Numeros!!\n Tente Novamente.\n")
            sleep(0.5)
        else:
            break
    sistema()


def execut():
    global user
    print("\n", "<"*4, "O que vc deseja que o Programa faça?", ">"*4)
    print("N°", " "*15, "Opções")
    for n, opcao in options.items():
        print(n, " "*2, opcao, "|")
    print("<"*7, "Digite o Numero Correspondente:", ">"*6)
    user = input("===> ")


print("-=" * 23)
print("   PROGRAMA DE RESOLUÇÃO DO DIAGRAMA DE VENN")
print("-=" * 23)
program()
execut()
resultado = resp(user, valores)
print(resultado)
