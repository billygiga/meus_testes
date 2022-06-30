from random import *


lista_num = sample(range(1,21),15)

#print(lista_num)

lista_float = [uniform(i,0) for i in lista_num]

#print(len(lista_float))

lista_par = [x for x in lista_num if x % 2 == 0]

lista_maior_que_dez = [i for i in lista_num if i > 10]

#print(lista_maior_que_dez)

lista_arredondada = [round(x) for x in lista_float]

#print(lista_arredondada)

lista_ord = [chr(i) for i in lista_num]

#print(lista_ord)

nome = [112,97,117,108,111,32,99,101,115,97,114 ]
for l in nome:
    print(chr(l),end='')