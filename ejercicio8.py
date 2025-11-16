def email_valido(email):
    return "@" in email


email = input("Ingresa tu dirección de email: ")

if email_valido(email):
    print("La dirección es válida.")
else:
    print("La dirección NO es válida.")
