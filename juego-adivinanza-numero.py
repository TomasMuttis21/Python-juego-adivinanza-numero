import random


def juego_adivinanza():
    # Generar un numero del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanza de numero!")
    print("Debes adivinar un numero del 1 al 100")
    print("Intenta adivinarlo!")

    while not adivinado:
        # Solicitar el numero del 1 al 100
        adivinanza = input("Introduzca un numero del 1 al 100: ")

        # Verificar que la entrada sea numero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Lo pasamos de texto a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero sectreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero sectreto es menor a {adivinanza}")
            else:
                print(
                    "Felicidades has ganado! El numero valido entre el 1 al 100"
                )
        else:
            print("Por favor introduzca un numero valido entre el 1 al 100")

juego_adivinanza()
