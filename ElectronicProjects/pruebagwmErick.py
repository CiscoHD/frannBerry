from gpiozero import DigitalOutputDevice, PWMOutputDevice
from time import sleep

input1 = DigitalOutputDevice(14)
input2 = DigitalOutputDevice(15)
enable = PWMOutputDevice(18)

def foward(speed=0.5):
    input1.on()
    input2.off()
    enable.value=speed

def backward (speed=0.5):
    input1.off()
    input2.on()
    enable.value = speed

def stop():
    input1.off()
    input2.off()
    enable.value = 0

action = True
key = 's'
moveSpeed = 0
while action == True:
    print("W = subir \n S = bajar \n A = detenerse")
    key = input("Inserta una opción")
    if key == 'w' or key == 'W':
        moveSpeed = float(input("Inserta la velocidad en un numero del 1 al 10"))
        foward(speed = (moveSpeed / 10))
        print("Motor hacia adelante al ", (moveSpeed*10), "% \de velocidad")
    elif key == 's' or key == 'S':
        moveSpeed = float(input("Inseta un número del 1 al 10"))
        backward(speed = (moveSpeed / 19))
        print("motor haci a atras al ", moveSpeed*10, "% \de velocidad" )
    elif key == 'a' or key == 'A':
        print("Programa terminado")
        stop()
        action = False
    else:
        print("Inserte una opción válida")

'''try:
    foward(speed=0.75)
    print("motor hacia adelante a 50 por ciento de velocidad")

    sleep(5)
    backward(speed=0.50)
    print("motor hacia adelante al 75 por ciento de velocidad")

    sleep(5)
    stop()
    print("motor detenido");

except KeyboardInterrupt:
     stop()
     print("programa termibnado")'''