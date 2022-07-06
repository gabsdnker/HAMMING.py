#descodificação do hamming

codigo_codificado= [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]

 #separar em 16 bits
 
# while codigo_codificado:
#      x= codigo_codificado[:16] 
    #  v= codigo_codificado[16:]


def desalternar_hamming(codigo_codificado): 
    #Reordena o codigo nos hammings que estavam alternados e coloca-os em uma lista ordenadamente

    codigo_separado = []
    lista_codigos_separados = []
    indice = 0
    quantificador = 0

    while codigo_codificado:

        quantidade_de_hamming = len(codigo_codificado)//16     

        if len(lista_codigos_separados) == quantidade_de_hamming:
            break
        elif len(codigo_separado) == 16:
            lista_codigos_separados.append(codigo_separado)
            codigo_separado = []
            quantificador += 1
            indice = 0
        else:        
            codigo_separado.append(codigo_codificado[(quantidade_de_hamming*indice)+quantificador])
            indice += 1

    return lista_codigos_separados

lista_codigos = desalternar_hamming(codigo_codificado)
for codigo_separado in lista_codigos:

    #soma os dígitos para descobrir os bits de paridade
    soma_digitos_paridade_1 = codigo_separado[3] + codigo_separado[7] + codigo_separado[11] + codigo_separado[15] + codigo_separado[5] + codigo_separado[9] + codigo_separado[13]
    soma_digitos_paridade_2 = codigo_separado[3] + codigo_separado[7] + codigo_separado[11] + codigo_separado[15] + codigo_separado[6] + codigo_separado[10] + codigo_separado[14]
    soma_digitos_paridade_4 = codigo_separado[5] + codigo_separado[6] + codigo_separado[7] + codigo_separado[12] + codigo_separado[13] + codigo_separado[14] + codigo_separado[15]
    soma_digitos_paridade_8 = codigo_separado[9] + codigo_separado[10] + codigo_separado[11] + codigo_separado[12] + codigo_separado[13] + codigo_separado[14] + codigo_separado[15]

    # determina se o bit de paridade está correto

    lista = [soma_digitos_paridade_1, soma_digitos_paridade_2, soma_digitos_paridade_4,soma_digitos_paridade_8]
    i= 0
    bits_com_erro= []
    bits_sem_erro= []

    for bit_paridade in lista:

        if bit_paridade%2==0:
            bit_paridade=0
        else:
            bit_paridade=1

    #coloca os bits com erro e sem erro em suas respectivas listas

        if bit_paridade != codigo_separado[2**i]:
            bits_com_erro.append(2**i)
        else: 
            bits_sem_erro.append(2**i)
        i+=1

    #determina se o bit de paridade 0 está certo  

    bit_paridade_0 = 0
    for bits in codigo_separado:        
        bit_paridade_0 += bits

    if bit_paridade_0%2==0:
        bit_paridade_0=0
    else:
        bit_paridade_0=1

    if bit_paridade_0 != codigo_separado[0]:
        bits_com_erro.append(bit_paridade_0)
    else:
        bits_sem_erro.append(bit_paridade_0)      

    if len(bits_com_erro) == 1:
        print(bits_com_erro[0])

    elif len(bits_com_erro)== 2:
        dicio = {1:{5,9,13,3,7,11,15}, 2:{6,10,14,3,7,11,15}, 4:{5,6,7,12,13,14,15}, 8:{8,9,10,11,12,13,14,15}}        
        x= dicio[bits_com_erro[0]] & dicio[bits_com_erro[1]]- dicio[bits_sem_erro[0]] - dicio[bits_sem_erro[1]]
        print(x)
    
    elif 
    



    
