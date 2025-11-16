numeros = [-5, -1, 0, 3, 7, -2, 10]


def es_positivo(x): return x > 0


positivos = list(filter(es_positivo, numeros))

print(positivos)
