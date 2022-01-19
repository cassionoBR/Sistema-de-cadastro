def leiaint(msg):

    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usúario optou por não informar o número\033[m')
            return 0
            break
        else:
            return n


def leiareal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsúario preferiu não digitar o número.\033[m')
            return 0
            break
        else: 
             return n
