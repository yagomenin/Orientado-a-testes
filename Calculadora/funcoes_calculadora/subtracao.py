from msg_print import msg_printar

from Mensagens.mensagens import msg_acabar


def subtrair():
    try:
        assert _subtrair_int(10, 5), 5
    except Exception:
        print("Erro nos testes")

    try:
        assert _subtrair_float(2.5, 1.5), 1.0
    except:
        print('Erro nos testes')

    try:
        assert _subtrair_none(None, None), Exception
    except Exception:
        print("O erro está vindo corretamente")









def _subtrair_int(n1, n2):
    print("Deve subtrair números inteiros que são 10 - 5 = 5")
    n1 - n2
    print(f'{n1 - n2}')
    msg_printar()
    return n1 - n2



def _subtrair_float(n1, n2):
    print("Deve Subtrair números float que são 2.5 e 1.5 = 1")
    n1 - n2
    print(f'{n1 - n2}')
    msg_printar()
    return n1 - n2



def _subtrair_none(n1, n2):
    print('Deve retornar um erro de None.')
    n1 - n2
    msg_acabar('Subtração')
    return Exception