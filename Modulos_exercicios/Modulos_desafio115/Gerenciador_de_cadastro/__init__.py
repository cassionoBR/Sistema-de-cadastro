def M_arquivo(n='', idade=''): 

    arquivo = open('Dados-desafio115.txt', 'a+')
    conteudo = arquivo.readlines()
    conteudo.append(f'\nNome: {n}. \t{idade} anos')
    
    arquivo = open('Dados-desafio115.txt', 'a')
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


