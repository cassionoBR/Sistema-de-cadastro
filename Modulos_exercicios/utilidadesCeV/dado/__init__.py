def leiadinheiro(n):
        param = False
        while not param:
                entrada = str(input(n)).strip().replace(',', '.')
                if entrada.isalpha() or entrada == '' or entrada == '.':
                        print(f'\033[31mERRO! "{entrada}" é um preço inválido\033[m')
                else:
                        param = True
                        return float(entrada)