from msg_print import msg_printar

from Mensagens.mensagens import msg_acabar


def somar():
    try:
        assert _somar_int(5, 5), 10
    except Exception:
        "Falha no teste"


    try:
        assert _somar_float(2.5, 2.5), 5
    except Exception:
        print("Erro nos testes")


    try:
        assert _soma_none(None, None), Exception
    except Exception as erro:
        print("Retornamos o erro corretamente.")





def _somar_int(n1, n2):
        print("Deve somar 5 + 5 = 10")
        n1 + n2
        print(f'{n1 + n2}')
        msg_printar()
        return n1 + n2



def _somar_float(n1, n2):
        print("Deve somar 2.5 + 2.5 = 5.0")
        n1 + n2
        print(f'{n1 + n2}')
        msg_printar()
        return n1 + n2



def _soma_none(n1, n2):
    n1 + n2
    print("Deve retornar um erro de None")
    msg_acabar('Soma')




