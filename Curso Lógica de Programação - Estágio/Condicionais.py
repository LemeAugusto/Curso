def penalzao(n):
    x = n
    x = x ** 2
    x = x/2
    print('O número calculado é: ', x)

limite = 5
nota = int(input('Nota: '))
folga = nota - limite

if nota >= limite:
    print('Passou!')
    penalzao(nota)
    print('Sobrou', folga, 'pontos')
else:
    print('Reprovou.')
    print('Faltou', folga, 'pontos.')

print('Finalizei')
