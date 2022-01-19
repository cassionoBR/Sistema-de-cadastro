def linhas(num=0):
    print('===' * num)


def menu(msg, f=False):

    mensagem = msg
    if f:
        mensagem = msg.upper()
    linhas(20)
    print(f'{mensagem}'.center(60))
    linhas(20)

def menu_opcoes(*msg):
    conteudo = list(msg)
    for i, c in enumerate(conteudo):
        print(f'{i + 1} - {c}')
    linhas(20)
