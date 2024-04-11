#        0  1  2  3  4   5   6   7   8   9
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

sub_lista = lista[4:8] #pegar parte específica da lista


     #início : termino  :  passo
#lista[  4   :    8     :    1  ]


sub_lista2 = lista[0:9:2]
sub_lista3 = lista[7:3:-1] #inverter lista
sub_lista4 = lista[9::-1] #ou sub_lista4 = lista[::-1]

print(lista)
print(sub_lista)
print(sub_lista2)
print(sub_lista3)
print(sub_lista4)
print("\n\n\n")


lista = [i for i in range(0,100)] #cria uma lista "automatica"

print(lista)