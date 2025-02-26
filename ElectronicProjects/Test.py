import gpiod
from time import sleep

# Definir el chip GPIO (usualmente 'gpiochip0' en Raspberry Pi)
chip = gpiod.Chip("gpiochip0")

# Definir los pines utilizados
MotorAIN1 = 17  # Pin de dirección 1
MotorAIN2 = 18  # Pin de dirección 2
MotorBIN1 = 22
MotorBIN2 = 23 

# Configurar los pines como salida
lines = chip.get_lines([MotorAIN1, MotorAIN2, MotorBIN1, MotorBIN2])
lines.request(consumer="motor_control", type=gpiod.LINE_REQ_DIR_OUT)

def menu():
    print("-----Programa piloto de subida de motor-------")
    print("u) Subir motores")
    print("d) Bajar motores")
    print("s) Parar motores")
    print("x) Salir")
    return input("Ingresa una opción ").lower()

def mover_motor(sentido):
    if sentido == 'u':
        print("Girando motor hacia arriba")
        lines.set_values([1, 0, 1, 0])
    elif sentido == 'd':
        print("Girando motor hacia abajo")
        lines.set_values([0, 1, 0, 1])
    elif sentido == 's':
        print("Motor detenido")
        lines.set_values([0, 0, 0, 0])
    else:
        print("Opción invalida")

try:
    while True:
        sentido = menu()
        if sentido != 'x':
            mover_motor(sentido)
        else :
            break
except KeyboardInterrupt:
    print("\nInterrupción del usuario")

finally:
    print("Finalizando programa")
    lines.set_values([0, 0, 0, 0])  # Apaga el motor
    lines.release()