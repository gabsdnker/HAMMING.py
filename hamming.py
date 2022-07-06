def dec_bin(numero):
    x = []
    while numero > 0:
            resto = numero % 2
            x.insert(0,resto)
            numero = numero // 2
    while len(x)!=8:
        x.insert(0,0)
    return x

def codificar_digitos_binarios(codigo):
    # soma os dígitos para descobrir os bits de paridade
    soma_digitos_paridade_0 = codigo[0] + codigo[3] + codigo[6] + codigo[10] + codigo[1] + codigo[4] + codigo[8]
    soma_digitos_paridade_1 = codigo[0] + codigo[3] + codigo[6] + codigo[10] + codigo[2] + codigo[5] + codigo[9]
    soma_digitos_paridade_3 = codigo[1] + codigo[2] + codigo[3] + codigo[7] + codigo[8] + codigo[9] + codigo[10]
    soma_digitos_paridade_7 = codigo[4] + codigo[5] + codigo[6] + codigo[7] + codigo[8] + codigo[9] + codigo[10]

    # determina se o bit de paridade é impar ou par
    lista = [soma_digitos_paridade_0, soma_digitos_paridade_1, soma_digitos_paridade_3,soma_digitos_paridade_7]
    y=0
    a=0
    for elemento in lista:
        if elemento%2==0:
            elemento=0
        else:
            elemento=1
        codigo.insert(y,elemento)
        y = y+2**a
        a+=1

    # determina o bit que vai ficar na posição zero do hamming
    soma = 0
    for elemento in codigo:
        soma+= elemento

    if soma%2==0:
        soma=0
    else:
        soma=1

    codigo.insert(0,soma)
    return codigo

def hamming_final(codigo):
    hamming_final= []
    # separa o código original em grupos de 11 bits e concatena o hamming codificado
    while len(codigo) != 0:
        while len(codigo)%11!=0:
            codigo.insert(0,0) 
        codigo_proximo = codigo[11:]
        codigo = codigo[:11]
        hamming = codificar_digitos_binarios(codigo)
        hamming_final.append(hamming)
        codigo = codigo_proximo
    return hamming_final

def resultado(codigo):
    # embaralha o hamming final
    h = hamming_final(codigo)
    resultado =[]
    x=0
    while x!=16:
        for lista in h:
            bit = lista[x]
            resultado.append(bit)
        x+=1
    return resultado

def main():
    codigo=[]
    with open("/home/aluno/Downloads/hamming/oi.txt","rb") as fonte, open("blue.txt","wb") as destino :
        while b := fonte.read(1):
            i = int.from_bytes(b,'little')
            # print(i)
            # print(dec_bin(i))
            codigo+=(dec_bin(i)) 
            destino.write(b)

    #print(codigo)
    print(resultado(codigo))

if __name__=='__main__':
    main()