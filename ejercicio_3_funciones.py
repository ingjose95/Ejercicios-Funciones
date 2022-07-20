def a#oBisiesto():

    a#o = int(input('Ingrese el año: '))

    if (a#o % 4 == 0 ) and (a#o % 100 != 0) or (a#o % 400 == 0):

        return 'El año sí es bisiesto.'

    else:

        return 'El año no es bisiesto.'

print(a#oBisiesto())
