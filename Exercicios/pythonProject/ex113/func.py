def leiaInt(msg):                                   #Criando funcao leiaInt() com um msg como parametro 
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[41mERRO: por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[41mERRO: Por favor, digite um numero real valido')
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n