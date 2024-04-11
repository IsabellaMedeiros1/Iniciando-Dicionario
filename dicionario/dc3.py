lista = []

for i in range (0,3):
    print('nome')
    nome = input()
    print("tel")
    tel = input()
    print('idade')
    idade = int(input())

    d = {'n': nome, 'tel': tel, "idade": idade}

    lista.append(d)

for i in range(0,3):
    d = lista[i]
    print('nome:', d['n'])
    print('tel:', d['tel'])
    print('idade:', d['idade'])


#Sistema para cadastrar as pessoas