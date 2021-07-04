#  000010000010 ADIÇÃO USANDO B1 E COSNTANTE 2 NO REGISTRADOR B2
#  001110101111 MULTIPLICAÇÃO USANDO B2 E COSNTANTE 15 NO REGISTRADOR L2
#  010001000010 SUBTRAÇÃO USANDO L1 E COSNTANTE 10 NO REGISTRADOR B1
#  011100000000 DIVISÃO USANDO B1 E COSNTANTE 0 NO REGISTRADOR L1
#  011100011110 DIVISÃO USANDO B1 E COSNTANTE 30 NO REGISTRADOR L1
#  100011001100 MAIOR USANDO L1 E COSNTANTE 12 NO REGISTRADOR B2
#  101011110100 MENOR USANDO L2 E COSNTANTE 20 NO REGISTRADOR B2

from Operations import docedeleite, alface, maisgordo, maismagro, brocolis, pizza
import pandas as pd

# FUNÇÕES
# 000 doce de leite
# 001 pizza
# 010 alface
# 011 brocolis
# 100 mais gordo
# 101 mais magro

tag = []
valid = []
data = []
tagdefinida = ['000', '001', '010', '011', '100', '101']


def initcache():
    for n in range(0, 4):
        data.append(0)
        valid.append(False)
        tag.append(-1)

umavez = True
turno = 1
initcache()


prossig = input("Prosseguir? y/n    ")
while prossig != "n":
    opcode = input("Entre com o OPCODE completo sem espaços: ")
    op = opcode[:3]
    rd = opcode[3:5]
    rs = opcode[5:7]
    const = opcode[7:12]
    data1 = opcode[:10]
    tagui = op

    b1 = 45
    b2 = 10
    l1 = 15
    l2 = 23


    def registradores(regis):
        if regis == "00":
            regist = b1
            end = "$b1"
        elif regis == "01":
            regist = b2
            end = "$b2"
        elif regis == "10":
            regist = l1
            end = "$l1"
        else:
            regist = l2
            end = "$l2"

        return end, regist


    def operacao(opera, turnodentro):
        x, y = registradores(rs)
        pos = -1
        hit = False

        if valid[0] == False and tag[0] != tagui and hit == False:
            if turnodentro == 1:
                print('Cache Miss!')
                valid[0] = True
                tag[0] = tagdefinida[0]
                data[0] = int(data1)
                valid[1] = True
                tag[1] = tagdefinida[1]
                data[1] = int(data1)
                valid[2] = True
                tag[2] = tagdefinida[2]
                data[2] = int(data1)
                valid[3] = True
                tag[3] = tagdefinida[3]
                data[3] = int(data1)

        for n in range(0, 4):
            pos += 1
            if valid[pos] and tag[pos] == tagui:
                print('Cache Hit!')
                hit = True
                break
            turnodentro = 2
        if hit == False:
            print('Cache Miss!')
            tag[0] = tagdefinida[4]
            data[0] = int(data1)
            tag[1] = tagdefinida[5]
            data[1] = int(data1)
            pos = -1
            for n in range(0, 4):
                pos += 1
                if valid[pos] and tag[pos] == tagui and hit == False:
                    print('Cache Hit!')
                    hit = True
                    break
        if hit == False:
            valid[0] = True
            tag[0] = tagdefinida[0]
            data[0] = int(data1)
            valid[1] = True
            tag[1] = tagdefinida[1]
            data[1] = int(data1)
            valid[2] = True
            tag[2] = tagdefinida[2]
            data[2] = int(data1)
            valid[3] = True
            tag[3] = tagdefinida[3]
            data[3] = int(data1)
            pos = -1
            for n in range(0, 4):
                pos += 1
                if valid[pos] and tag[pos] == tagui and hit == False:
                    print('Cache Hit!')
                    hit = True
                    break
        if hit:
            if int(opera) % 2 == 0:
                if opera == "000":
                    resp = docedeleite(y, const)
                    ope = "Doce de Leite"
                elif opera == "010":
                    resp = alface(y, const)
                    ope = "Alface"
                else:
                    resp = maisgordo(y, const)
                    ope = "Mais Gordo"
            else:
                if opera == "001":
                    resp = pizza(y, const)
                    ope = "Pizza"
                elif opera == "011":
                    resp = brocolis(y, const)
                    ope = "Brócolis"
                else:
                    resp = maismagro(y, const)
                    ope = "Mais Magro"
            print(
                "\nSalvando o resultado de\033[1m",
                resp,
                "\033[0mno registrador ",
                registradores(rd)[0],
                "\n",
            )
            return ope
        else:
            operacao(opera, turnodentro)


    print("OP = ", op, "=> ", operacao(op, turno))
    print("REGISTRADOR DESTINO = ", registradores(rd)[0])
    print("REGISTRADOR FONTE = ", registradores(rs)[0])
    print("CONSTANTE = ", int(const, 2))

    prossig = input("\nProsseguir? y/n    ")
