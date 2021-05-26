from msg_print import msg_printar

from Mensagens.mensagens import msg_acabar


def multiplicar():
    try:
        assert _multiplicar_int(7, 2), 14
    except Exception:
        print("Falha no teste")

    try:
        assert _multiplicar_float(2.5, 2.5), 6.25
    except Exception:
        print("Erro nos testes")



    try:
        assert _multiplicar_none(None, None), Exception
    except Exception:
        print("Retornamos o erro de None corretamente.")


def _multiplicar_int(n1, n2):
    print("Deve multiplicar 7 * 2 = 14")
    n1 / n2
    print(f'{n1 * n2}')
    msg_printar()
    return n1 * n2


def _multiplicar_float(n1, n2):
    print("Deve multiplicar 2.5 * 2.5 = 6.25")
    n1 * n2
    print(f'{n1 * n2}')
    msg_printar()
    return n1 * n2



def _multiplicar_none(n1, n2):
    n1 * n2
    msg_acabar("Multiplicação")
    print("Deve retornar um erro de None")
    return n1 * n2




