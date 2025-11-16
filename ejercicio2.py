def calcular_area_rectangulo(anchura, altura):
    return anchura * altura


anchura = float(input("Ingresa la anchura del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

area = calcular_area_rectangulo(anchura, altura)

print("El área del rectángulo es:", area)
