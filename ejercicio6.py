def suma_recursiva(n):
    if n == 1:
        return 1
    return n + suma_recursiva(n - 1)


print(suma_recursiva(5))
