def metade(n=0, conv=True):
    """
    -> Função: dividir (n) pela metade
    :param n: numero à ser tratado
    :return: metade de (n)
    """
    if n is int:
        resposta = int(n) / 2
    else:
        resposta = float(n) / 2
    if conv:
        return conversor(resposta)
    else:
        return resposta


def dobro(n=0, conv=True):
    """
    -> Função: Dobrar (n)
    :param n: Número à ser tratado
    :return: Dobro de (n)
    """
    if n is int:
        num = int(n)
    else:
        num = float(n)
    resposta = num * 2
    if conv:
        return conversor(resposta)
    else:
        return resposta


def aumentar(n=0, p=0, conv=True):
    """
    -> Função: Aumentar (n) pela porcentagem (p) indicada
    :param n: Número à ser tratado
    :param p: valor da porcentagem
    :return: Valor da porcentagem de (n)
    """
    if n is int:
        num = int(n)
    else:
        num = float(n)
    porcentagem = ((p/100) * num)
    resposta = num + porcentagem
    if conv:
        return conversor(resposta)
    else:    
        return resposta


def diminuir(n=0, p=0, conv=True):
    """
    -> Função: Reduzir (n) pela porcetagem (p) indicada.
    :param n: Número à ser tratado
    :param p: Valor da porcentagem
    :return: Valor da redução de (n) por (p)
    """
    if n is int:
        num = int(n)
    else:
        num = float(n)
    porcentagem = ((p/100) * num)
    resposta = num - porcentagem
    if conv:
        return conversor(resposta)
    else:    
        return resposta
    

def conversor(n=0, moedas='R$'):
    if n is int:
        num = int(n)
    else:
        num = float(n)
    return f'{moedas}{num:.2f}'


def resumo(numero=0, p1=0, p2=0):
    print('===' * 20)
    print(f'{"Resumo do valor"}'.center(60))
    print('===' * 20)
    print(f'Preço analisado: \t{conversor(numero)}')
    print(f'Dobro do preço: \t{dobro(numero)}')
    print(f'Metade do preço: \t{metade(numero)}')
    print(f'{p1}% de aumento: \t{aumentar(numero, p1)}')
    print(f'{p2}% de redução: \t{diminuir(numero, p2)}')
    print(f'===' * 20)