from fileinput import close
from time import sleep


def menu(msg, f=False):
    mensagem = msg
    if f:
        mensagem = msg.upper()
    print('===' * 20)
    print(f'{mensagem}'.center(60))
    print('===' * 20)


def M_arquivo(n='', idade=''):
    arquivo = open('Dados-desafio115.txt', 'r')
    conteudo = arquivo.readlines()
    conteudo.append(f'\nNome: {n} \t{idade} anos')
    
    arquivo = open('Dados-desafio115.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

def cadastro():
    cadastro = dict()
    while True:
        cadastro['Nome: '] = str(input('Nome: '))
        try:
            idade = int(input('Idade: '))
        except(TypeError, ValueError, KeyboardInterrupt):
                print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
        else:
            cadastro['Idade: '] = idade
            print(f'Novo registro de {cadastro["Nome: "]} adicionado.')
            M_arquivo(cadastro['Nome: '], cadastro['Idade: '])
            cadastro.clear
            break
                        

def leia_dados():
    arquivo = open('Dados-desafio115.txt', 'r')
    ler = arquivo.readlines()
    for c in ler:
        print(c, end='')
    print()    
    arquivo.close


def programa_master():
    while True:
        menu('Menu principal', True)
        print('''>>> 1 - Ver pessoas cadastradas
>>> 2 - Cadastrar nova pessoa
>>> 3 - Sair do programa''')
        print('===' * 20)
        sleep(0.7)
        try:
            usuario = int(input('Sua opção: '))
        except(TypeError, ValueError, KeyboardInterrupt):
            print('\033[31mERRO! por favor digite um número inteiro válido.\033[m')
        else:
            while usuario > 3 or usuario == 0:
                print('\033[31mERRO! digite uma opção válida!\033[m')
                usuario = int(input('Sua opção: '))
            if usuario == 1:
                sleep(0.7)
                menu('Pessoas cadastradas', True)
                leia_dados()
            elif usuario == 2:
                cadastro()
                sleep(0.7)
            else:
                if usuario == 3:
                    sleep(0.7)
                    print('Até mais...')
                    sleep(0.3)
                    print('Programa finalizado.')
                    break     