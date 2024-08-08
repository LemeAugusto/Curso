aluno = {'nome': 'Joviano', 'cursos': '20', 'idade': 25}
aluno.keys() # dict_keys(['nome', 'cursos', 'idade'])
aluno.get('nome') # Joviano
# aluno.get(altura) # Error

nota = aluno.get('nota')
aluno_nome = aluno.get('nome')
def penalzao(n):
    x = n
    x = x ** 2
    x = x/2
    print('O número calculado é: ', x)

limite = 5
folga = nota - limite

if nota >= limite:
    print('Passou!')
    print('Sobrou', folga, 'pontos')
    print(aluno_nome, nota, 'apr.txt')
else:
    print('Reprovou.')
    print('Faltou', folga, 'pontos.')
print(aluno_nome, nota, 'apr.txt')

print('Finalizei')
