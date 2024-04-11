d1={'nome': 'maria', 'tel': '(11) 11111-1111'}
d2={'nome': 'joao', 'tel': '(22) 22222-2222'}

lista =[]
lista.append(d1)    # add no indice 0
lista.append(d2)    # add no indice 1

d = lista[1]     #mostrar dicionario especifico
print('nome:', d['nome'])
print('tel:', d['tel'])
print("\n\n")

for i in range(0,2):   #for p mostrar os dois dicionario
    d = lista[i]
    print('nome:', d['nome'])
    print('tel:', d['tel'])