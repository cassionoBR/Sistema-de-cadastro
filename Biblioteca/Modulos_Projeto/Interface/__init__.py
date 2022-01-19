def linhas(num=0):
    print('===' * num)


def menu(msg, f=False):

    mensagem = msg
    if f:
        mensagem = msg.upper()
    linhas(20)
    print(f'\033[92;47m {mensagem} \033[m'.center(70))
    linhas(20)

def menu_opcoes(*msg):
    conteudo = list(msg)
    for i, c in enumerate(conteudo):
        print(f'\033[1;92m{i + 1}\033[m - {c}')
    linhas(20)
