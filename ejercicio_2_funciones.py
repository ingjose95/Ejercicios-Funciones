def numeroPrimo(numero, divisor):

    if numero % divisor == 0 and numero // 1 == numero:

        return True

    else:

        return False

print(numeroPrimo(72,20))