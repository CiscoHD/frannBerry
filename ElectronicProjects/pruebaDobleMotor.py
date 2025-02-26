import gpiozero as gpio
from time import sleep

input1 = gpio.DigitalOutputDevice(14)
input2 = gpio.DigitalOutputDevice(15)
enable1 = gpio.PWMOutputDevice(18)
enable2 = gpio.PWMOutputDevice(13)

def foward(speed1, speed2):
    input1.on()
    input2.off()
    enable1.value = speed1
    enable2.value = speed2

def backward(speed1, speed2):
    input1.off()
    input2.on()
    enable1.value = speed1
    enable2.value = speed2

def stop():
    input1.off()
    input2.off()
    enable1.value = 0
    enable2.value = 0

option = 'q'
speed1 = 0;
speed2 = 0;

while option != 'a':
    print("W - subir \n S - bajar \n A - detenerse")
    option = input("Inserte una opción")

    if option == 'w' or option == 'W':
        speed1 = float(input("velocidad del motor 1 "))
        speed2 = float(input("velocidad del motor 2 "))
        foward(speed1, speed2)
    elif option == 's' or option == 'S':
        speed1 = float(input("velocidad del motor 1 "))
        speed2 = float(input("velocidad del motor 2 "))
        backward(speed1, speed2)
    elif option == 'a' or option == 'A':
        print("programa terminado")
    else: 
        print("inserte una opción válida")
