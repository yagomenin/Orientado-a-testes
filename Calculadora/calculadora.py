from Calculadora.funcoes_calculadora.divisao import dividir
from Calculadora.funcoes_calculadora.multiplicacao import multiplicar
from Calculadora.funcoes_calculadora.soma import somar
from Calculadora.funcoes_calculadora.subtracao import subtrair


def calculadora():
    try:
        somar()
    except Exception as error:
        print("Algum erro aconteceu", error)
    else:
        print("======================= Testes Soma OK ==========================")


    try:
        subtrair()
    except Exception as error:
        print("Algum erro aconteceu", error)
    else:
        print("======================= Testes Subtração OK ==========================")


    try:
        dividir()
    except Exception as error:
        print('Algum erro aconteceu', error)
    else:
        print("======================= Testes Divisão OK ==========================")

    try:
        multiplicar()
    except Exception as error:
        print('Algum erro aconteceu', error)
    else:
        print("======================= Testes Multiplicação OK ==========================")












