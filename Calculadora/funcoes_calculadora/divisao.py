from msg_print import msg_printar

from Mensagens.mensagens import msg_acabar


def dividir():
    try:
        assert _dvidir_int(10, 2), 5
    except Exception:
        "Falha no teste"

    try:
        assert _dividir_float(8.5, 2.5), 3.4
    except Exception:
        print("Erro nos testes")

    try:
        assert _divisao_zero(0, 3), ZeroDivisionError
    except AssertionError:
        print("Se caiu aqui, O erro não foi o certo")
    else:
        print("Erro de divisão por 0, tratado corretamente")

    try:
        assert _divisao_none(None, None), Exception
    except Exception:
        print("Retornamos o erro de None corretamente.")


def _dvidir_int(n1, n2):
    print("Deve dividir 10 / 2 = 5")
    n1 / n2
    print(f'{n1 / n2}')
    msg_printar()
    return n1 / n2


def _dividir_float(n1, n2):
    print("Deve dividir 8.5 / 2.5 = 3.4")
    n1 / n2
    print(f'{n1 / n2}')
    msg_printar()
    return n1 / n2


def _divisao_zero(n1, n2):
    print("Deve dar erro de divisao por 0")
    n1 / n2
    msg_printar()
    return Exception



def _divisao_none(n1, n2):
    n1 / n2
    print("Deve retornar um erro de None")
    msg_acabar('Divisão')
    return Exception
