
import random
numero_adivinar = random.randint(1,10)
intentos = 5
introducir = int(input("un número del 1 al 10: "))


if numero_adivinar == introducir:
    print("es el numero")
else:
    while numero_adivinar != introducir or intentos != 0:
        if numero_adivinar == introducir:
            print("es el numero")
            break
        else:
            print("no es el numero")
            print("hacer",intentos,"intentos")
            intentos -= 1
        if intentos == 0:
            print("perdiste")
            break
        if numero_adivinar > introducir:
            print("es un numero mas grande de", introducir)
        if numero_adivinar < introducir:
            print("es un número mas pequeño que el", introducir)
        introducir = int(input("digamos un número del 1 al 10: "))
