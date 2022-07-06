codigo_codificado= [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0,1]
print(len(codigo_codificado))

bits_não_paridades = {3,5,6,7,9,10,11,12,13,14,15,16}

bits_com_erro= []

dicio = {1:{5,9,13,3,7,11,15}, 2:{6,10,14,3,7,11,15}, 4:{5,6,7,12,13,14,15}, 8:{8,9,10,11,12,13,14,15}}

x = dicio[4]
y = dicio[1]
z = dicio[8]
k = dicio[2]
print(x & y - z - k)




