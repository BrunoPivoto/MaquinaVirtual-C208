def docedeleite(valo, consta):
    resultado = (valo + int(consta, 2))
    print('\n', valo, ' + ', int(consta, 2))
    return resultado


def pizza(valo, consta):
    resultado = (valo * int(consta, 2))
    print('\n', valo, ' x ', int(consta, 2))
    return (resultado)


def alface(valo, consta):
    resultado = (valo - int(consta, 2))
    print('\n', valo, ' - ', int(consta, 2))
    return (resultado)


def brocolis(valo, consta):
    if int(consta, 2) != 0:
        resultado = (valo / int(consta, 2))
        print('\n', valo, ' / ', int(consta, 2))
    else:
        resultado = 'Não existe divisão por 0'
    return (resultado)


def maisgordo(valo, consta):
    print('\n', valo, ' > ', int(consta, 2), '??')
    if (valo > int(consta, 2)):
        return ("Você é mais gordo")
    else:
        return ("Você não é mais gordo")


def maismagro(valo, consta):
    print('\n', valo, ' < ', int(consta, 2), '??')
    if (valo < int(consta, 2)):
        return ("Você é mais magro")
    else:
        return ("Você não é mais magro")
