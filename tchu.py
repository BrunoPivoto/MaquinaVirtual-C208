def docedeleite(valo, consta):
    resultado = (int(valo, 2) + int(consta, 2))
    return resultado

def pizza(valo, consta):
    resultado = (int(valo, 2) * int(consta, 2))
    return(resultado)

def alface(valo, consta):
    resultado = (int(valo, 2) - int(consta, 2))
    return(resultado)

def brocolis(valo, consta):
    resultado = (int(valo, 2) / int(consta, 2))
    return(resultado)

def maisgordo(valo, consta):
    if (int(valo, 2) > int(consta, 2)):
        return("Você é mais gordo")
    else:
        return("Você não é mais gordo")

def maismagro(valo, consta):
    if (int(valo, 2) < int(consta, 2)):
        return("Você é mais magro")
    else:
        return("Você não é mais magro")
