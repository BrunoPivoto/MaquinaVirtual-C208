#  000010000010
from tchu import docedeleite, alface, maisgordo, maismagro, brocolis, pizza

opcode = input("Entre com o OPCODE completo sem espaços: ")
op = opcode[:3]
rd = opcode[3:5]
rs = opcode[5:7]
const = opcode[7:12]
valor = "11"


def registradores(regis):
    if regis == '00':
        regist = '$b1'
    elif regis == '01':
        regist ='$b2'
    elif regis == '10':
        regist = '$l1'
    else:
        regist = '$l2'

    return regist





def operacao(opera):
    if int(opera) % 2 == 0:
        if opera == '000':
            resp = docedeleite(valor, const)
        elif opera == '010':
            resp = alface(valor, const)
        else:
            resp = maisgordo(valor, const)
    else:
        if opera == '001':
            resp = pizza(valor, const)
        elif opera == '011':
            resp = brocolis(valor, const)
        else:
            resp = maismagro(valor, const)

    print('Salvando o resultado de ', resp, 'no registrador ', registradores(rd))
    # , 'no registro ', registradores(rd)



operacao(op)


print('OP = ', op)
print('REGISTRADOR DESTINO = ', rd, 'que é ', registradores(rd))
print('REGISTRADOR FONTE = ', rs, 'que é ', registradores(rs))
print('CONSTANTE = ', const, 'que é ', int(const, 2))









