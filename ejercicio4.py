def pares(n, m):

    if not (n > 0 and m > 0 and n < m):
        raise Exception("No es posible continuar con la operación")

    # Generamos los números pares
    for numero in range(n, m + 1):
        if numero % 2 == 0:
            yield numero


try:
    for p in pares(3, 12):
        print(p)
except Exception as e:
    print(e)
