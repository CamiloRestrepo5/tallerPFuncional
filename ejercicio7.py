def obtener_identificador(nombre_completo, dni):
    partes = nombre_completo.split()

    primer_nombre = partes[0]
    apellido = partes[-1]

    largo_apellido = len(apellido)
    primeros_dni = dni[:3]

    return f"{primer_nombre}{largo_apellido}{primeros_dni}"


while True:
    nombre = input(
        "Ingrese nombre completo del socio (o vacío para terminar): ").strip()

    if nombre == "":
        print("Procesamiento finalizado.")
        break

    # Validación de DNI
    dni = input("Ingrese el DNI: ").strip()
    while not (dni.isdigit() and 7 <= len(dni) <= 8):
        print("DNI inválido. Debe tener 7 u 8 dígitos.")
        dni = input("Ingrese el DNI nuevamente: ").strip()

    identificador = obtener_identificador(nombre, dni)
    print("Identificador generado:", identificador)
    print()
