from time import sleep
from connection import options, resp
from os import system
import platform

op = False
if platform.system() == 'Windows':
    op = True


def clear():
    if op:
        return system('cls')
    return system('clear')


def program():
    global valores
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
            clear()
            print("Utilize apenas Numeros!!\n Tente Novamente.\n")
            sleep(0.4)
            return program()
    clear()


def execut():
    global user
    print("\n", "<"*4, "O que vc deseja que o Programa faça?", ">"*4)
    print("         Para sair digite 'exit' :D")
    print("N°", " "*15, "Opções")
    for n, opcao in options.items():
        print(n, " "*2, opcao, "|")
    print("<"*7, "Digite o Numero Correspondente:", ">"*6)
    user = str(input("===> ")).strip().lower()

clear()
print("-=" * 23)
print("   PROGRAMA DE RESOLUÇÃO DO DIAGRAMA DE VENN")
print("-=" * 23, "\n")
program()
while True:
    clear()
    execut()
    if user == "exit":
        sleep(0.3)
        clear()
        sleep(0.3)
        print("Volte logo :D\n"
              "Contribuidores:\n"
              "Alexandre Oliver\n"
              "Richard Smanhoto")
        exit()
    resultado = resp(user, valores)
    print(resultado)
    input()
