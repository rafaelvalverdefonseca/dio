menu = '''
    #################################
    Digite a opção desejada:
    [S] = Saque
    [D] = Deposito
    [E] = Extrato
    [x] = Sair
    ##################################
'''
saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    entrada = input(menu).upper()
    ## SAQUE
    if entrada == 'S':
        saque = float(input('Digite o valor do saque: '))
        if saque > limite:
            print('Valor do saque acima do limite permitido.')
            saque = float(input('Digite o valor do saque: '))
        else:
            if saque > saldo:
                print(f'Você não tem saldo para realizar essa operação. Seu saldo é R$ {saldo:.2f}')
            else:
                if LIMITE_SAQUE == numero_saque:
                    print(F'Você já realizou {LIMITE_SAQUE} saques. Limite de saque excedido')
                else:
                    if saque <= 0:
                        print('Valor do saque invalido')
                    else:
                        saldo = saldo - saque
                        print(f'O saque no valor de R$ {saque:.2f} confirmado. \nSeu saldo é R$ {saldo:.2f}')
                        extrato += f'Saque realizado: R$ {saque:.2f}\n'
                        numero_saque += 1
    ## DEPOSITO
    elif entrada == 'D':
        deposito = float(input('Digite o valor do deposito: '))
        if deposito <= 0:
            print('Valor digitado inválido.')
        else:
            saldo += deposito
            print(f'Valor depositado: R$ {deposito:.2f}. \nSeu saldo é: R$ {saldo:.2f}')
            extrato += f'Deposito realizado: R$ {deposito:.2f}\n'
    ## EXTRATO
    elif entrada == 'E':
        print('\n######EXTRATO######')
        print('Sm movimentação' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('######EXTRATO######')
    ## SAIR DO SISTEMA
    elif entrada == 'X':
        print('Saindo...')
        break
    else:
        print(f'Você digitou a opção {entrada}. Opção digitada inválida. Tente novamente!')
