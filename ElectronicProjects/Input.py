from gpiozero import Button
from time import sleep

arriba  = Button(2)
abajo = Button(3)

while True:
    sentido = input("Ingresa una opción: ").lower()
    if arriba.value == 0:
        print("Puente puede subir")
    elif arriba.value == 1:
        print("Puente bloquedo arriba")
    if abajo.value == 0:
        print("Puente puede bajar ")
    elif abajo.value == 1:
        print("Puente bloquedo abajo")
    else :
        print("error")
    sleep(1)