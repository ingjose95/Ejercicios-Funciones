def añoBisiesto(año):

    if año >= 366:

        return 'El año es bisiesto.'

    else:

        return 'El año no es bisiesto.'

print(añoBisiesto(366))

print(añoBisiesto(365))