from Modulos_exercicios.Modulos_desafio115 import Interface
from Modulos_exercicios.Modulos_desafio115 import Gerenciador_de_cadastro
from time import sleep

while True:
    Interface.menu('Sistema de cadastro', True)
    Interface.menu_opcoes('Ver pessoas cadastradadas.', 'Cadastrar uma nova pessoa.', 'Sair do programa.')
    sleep(1.3)
    try:
        usuario = int(input(f'{"Sua opção: "}'))
        Interface.linhas(20)
        sleep(1.3)
    except (TypeError, ValueError, KeyboardInterrupt):
        print('\033[31mERRO, digite um número inteiro válido!\033[m')
    else:
        if usuario == 1:
            Interface.menu('Pessoas cadastradas', True)
            Gerenciador_de_cadastro.leia_dados()
        elif usuario == 2:
            Interface.menu('cadastrar nova pessoa', True)
            Gerenciador_de_cadastro.cadastro()
        elif usuario == 3:
            Interface.menu('Até mais! tenha um excelente dia.')
            break
        else:
            Interface.linhas(20)
            print('\033[31mERRO! Você digitou uma opção inválida!\033[m')
