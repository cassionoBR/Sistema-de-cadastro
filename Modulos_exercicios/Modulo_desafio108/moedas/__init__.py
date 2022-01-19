def metade(n=0, conv=True):
    """
    -> Função: dividir (n) pela metade
    :param n: numero à ser tratado
    :return: metade de (n)
    """
    if conv:
        return f'{n / 2:.2f}'
    else:
        return n / 2


def dobro(n=0, conv=True):
    """
    -> Função: Dobrar (n)
    :param n: Número à ser tratado
    :return: Dobro de (n)
    """
    if conv:
        return f'R${n * 2:.2f}'
    else:
        return n * 2


def aumentar(n=0, p=0, conv=True):
    """
    -> Função: Aumentar (n) pela porcentagem (p) indicada
    :param n: Número à ser tratado
    :param p: valor da porcentagem
    :return: Valor da porcentagem de (n)
    """
    porcentagem = ((p/100) * n)
    if conv:
        return f'R${n + porcentagem:.2f}'
    else:    
        return n + porcentagem


def diminuir(n=0, p=0, conv=True):
    """
    -> Função: Reduzir (n) pela porcetagem (p) indicada.
    :param n: Número à ser tratado
    :param p: Valor da porcentagem
    :return: Valor da redução de (n) por (p)
    """
    porcentagem = ((p/100) * n)
    if conv:
        return f'R${n - porcentagem:.2f}'
    else:    
        return n - porcentagem
    

def conversor(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'
