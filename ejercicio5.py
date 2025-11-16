def imprimir_resultado(func):
    def wrapper(*args):
        print("Resultado:", func(*args))
    return wrapper


@imprimir_resultado
def sumar(a, b):
    return a + b


sumar(3, 4)
