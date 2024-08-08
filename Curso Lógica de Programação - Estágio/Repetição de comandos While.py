while True:
    x = input('Digite sua senha: ')
    if x == 'banana':
        print('Senha ok!')
        break
    else:
        print('Senha incorreta! Tente novamente')
        print('.' * 10)