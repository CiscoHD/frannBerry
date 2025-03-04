import gpiozero as gpio
from time import sleep

input1 = gpio.DigitalOutputDevice(14)
input2 = gpio.DigitalOutputDevice(15)
enable1 = gpio.PWMOutputDevice(18) #Motor1
enable2 = gpio.PWMOutputDevice(13) #Motor2

servo = gpio.Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

def menu():
    print("-----Puente de elevación-------")
    print("w) Subir motores")
    print("s) Bajar motores")
    print("q) Parar motores")
    print("a) Modificar velocidad del motor 1")
    print("d) Modificar velocidad del motor 2")
    print("e) Salir")
    return input("Ingresa una opción: ").lower()

def moverPlataforma(opcion):
    if opcion == 'w':
        cerrar_pluma()
        print("Elevando plataforma")
        enable1.value = 1
        enable2.value = 1  
        input1.on()
        input2.off()
    elif opcion == 's':
        print("Bajando plataforma")
        enable1.value = 1
        enable2.value = 1
        input1.off()
        input2.on()
        abrir_pluma()
    elif opcion == 'a':
        enable1.value = float(input("velocidad del motor 1 ")) / 10
    elif opcion == 'd':
        enable2.value = float(input("velocidad del motor 2 ")) / 10
    elif opcion == 'q':
        print("Motor detenido")
        input1.off()
        input2.off()
    else:
        print("Opción invalida")

def abrir_pluma():
    #Mueve el servomotor de 0° a 90° simulando la apertura de la pluma.
    print("Pluma abierta (90°)")
    servo.value = 0  # Posición intermedia (90°)
    sleep(1)

def cerrar_pluma():
    #Mueve el servomotor de 90° a 0° simulando el cierre de la pluma.
    print("Pluma cerrada (0°)")
    servo.value = -1  # Mitad del recorrido (-0.5 equivale a 0° en este caso)
    sleep(1)

try: 
    while True: 
        sentido = menu()
        if sentido != 'e':
            moverPlataforma(sentido)
        else : 
            break
except KeyboardInterrupt:
    print("Interrupción del usuario")

finally:
    print("Finalizando programa")
    input1.off()
    input2.off()
    enable1.value = 0
    enable2.value = 0