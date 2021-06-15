#  000010000010 ADIÇÃO USANDO B1 E COSNTANTE 2 NO REGISTRADOR B2
#  001110101111 MULTIPLICAÇÃO USANDO B2 E COSNTANTE 15 NO REGISTRADOR L2
#  010001000010 SUBTRAÇÃO USANDO L1 E COSNTANTE 10 NO REGISTRADOR B1
#  011100000000 DIVISÃO USANDO B1 E COSNTANTE 0 NO REGISTRADOR L1
#  011100011110 DIVISÃO USANDO B1 E COSNTANTE 30 NO REGISTRADOR L1
#  100011001100 MAIOR USANDO L1 E COSNTANTE 12 NO REGISTRADOR B2
#  101011110100 MENOR USANDO L2 E COSNTANTE 20 NO REGISTRADOR B2
from operations import docedeleite, alface, maisgordo, maismagro, brocolis, pizza

#FUNÇÕES
#000 doce de leite
#001 pizza
#010 alface
#011 brocolis
#100 mais gordo
#101 mais magro

prossig = input('Prosseguir? y/n    ')
while prossig != 'n':
    opcode = input("Entre com o OPCODE completo sem espaços: ")
    op = opcode[:3]
    rd = opcode[3:5]
    rs = opcode[5:7]
    const = opcode[7:12]

    #Valores prefixados, sinta-se livre para alterar
    b1 = 45
    b2 = 10
    l1 = 15
    l2 = 23


    def registradores(regis):
        if regis == '00':
            regist = b1
            end = '$b1'
        elif regis == '01':
            regist = b2
            end = '$b2'
        elif regis == '10':
            regist = l1
            end = '$l1'
        else:
            regist = l2
            end = '$l2'

        return end, regist


    def operacao(opera):
        x, y = registradores(rs)
        if int(opera) % 2 == 0:
            if opera == '000':
                resp = docedeleite(y, const)
                ope = "Doce de Leite"
            elif opera == '010':
                resp = alface(y, const)
                ope = "Alface"
            else:
                resp = maisgordo(y, const)
                ope = "Mais Gordo"
        else:
            if opera == '001':
                resp = pizza(y, const)
                ope = "Pizza"
            elif opera == '011':
                resp = brocolis(y, const)
                ope = "Brócolis"
            else:
                resp = maismagro(y, const)
                ope = "Mais Magro"

        print('\nSalvando o resultado de\033[1m', resp, '\033[0mno registrador ', registradores(rd)[0], '\n')
        return ope


    print('OP = ', op, '=> ', operacao(op))
    print('REGISTRADOR DESTINO = ', registradores(rd)[0])
    print('REGISTRADOR FONTE = ', registradores(rs)[0])
    print('CONSTANTE = ', int(const, 2))

    prossig = input('\nProsseguir? y/n    ')