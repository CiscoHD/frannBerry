import gpiozero as gpio
from time import sleep

output1 = gpio.DigitalOutputDevice(14)
output2 = gpio.DigitalOutputDevice(15)
enable1 = gpio.PWMOutputDevice(18) #Motor1
enable2 = gpio.PWMOutputDevice(13) #Motor2

servo = gpio.Servo(23, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

up_arrived = gpio.Button(2)
down_arrived = gpio.Button(3)

def menu():
    print("-----Puente de elevación-------")
    print("w) Subir motores")
    print("s) Bajar motores")
    print("q) Parar motores")
    print("a) Modificar velocidad del motor 1")
    print("d) Modificar velocidad del motor 2")
    print("e) Salir")
    return input("Ingresa una opción: ").lower()

def elevar_plataforma():
    print("Elevando plataforma")
    enable1.value = 1
    enable2.value = 1  
    output1.on()
    output2.off()

def bajar_plataforma():
    print("Bajando plataforma")
    enable1.value = 1
    enable2.value = 1
    output1.off()
    output2.on()

def abrir_pluma():
    """Mueve el servomotor de 0° a 90° simulando la apertura de la pluma."""
    print("🟢 Pluma abierta (90°)")
    servo.value = 0  # Posición intermedia (90°)
    sleep(1)

def cerrar_pluma():
    """Mueve el servomotor de 90° a 0° simulando el cierre de la pluma."""
    print("🔴 Pluma cerrada (0°)")
    servo.value = -1  # Mitad del recorrido (-0.5 equivale a 0° en este caso)
    sleep(1)

try: 
    while True: 
        sentido = menu()
        if sentido != 'e':
            if sentido == 'w' and not up_arrived.is_pressed:
                elevar_plataforma()
                cerrar_pluma()
            elif up_arrived.is_pressed:
                print("La plataforma ya está arriba")
            if sentido == 's' and not down_arrived.is_pressed: 
                bajar_plataforma()
            elif down_arrived.is_pressed:
                print("La plataforma ya está abajo")
            elif sentido == 'q':
                print("Motor detenido")
                output1.off()
                output2.off()
        else : 
            break
        if down_arrived == 1:
            abrir_pluma()    
except KeyboardInterrupt:
    print("Interrupción del usuario")

finally:
    print("Finalizando programa")
    output1.off()
    output2.off()
    enable1.value = 0
    enable2.value = 0