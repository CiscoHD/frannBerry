# Programa: motor_gpiod.py
# Controla un motor DC con el puente H L293D en Raspberry Pi usando gpiod

import gpiod
from time import sleep

# Definir el chip GPIO (usualmente 'gpiochip0' en Raspberry Pi)
chip = gpiod.Chip("gpiochip0")

# Definir los pines utilizados
MotorIN1 = 15  # Pin de dirección 1
MotorIN2 = 14  # Pin de dirección 2
MotorE1 = 18   # Pin de habilitación

# Configurar los pines como salida
lines = chip.get_lines([MotorIN1, MotorIN2, MotorE1])
lines.request(consumer="motor_control", type=gpiod.LINE_REQ_DIR_OUT)

# Función para controlar el motor
def mover_motor(sentido):
    if sentido == "adelante":
        print("Girando motor en un sentido por 5 segundos")
        lines.set_values([1, 0, 1])  # IN1 = HIGH, IN2 = LOW, Enable = HIGH
    elif sentido == "atras":
        print("Girando motor en sentido contrario por 5 segundos")
        lines.set_values([0, 1, 1])  # IN1 = LOW, IN2 = HIGH, Enable = HIGH

    sleep(5)
    print("Deteniendo motor")
    lines.set_values([0, 0, 0])  # Desactiva el motor
    sleep(1)

try:
    mover_motor("adelante")  # Girar hacia adelante
    mover_motor("atras")  # Girar hacia atrás

except KeyboardInterrupt:
    print("\nInterrupción del usuario")

finally:
    print("Finalizando programa")
    lines.set_values([0, 0, 0])  # Apaga el motor
    lines.release()  # Libera los pines


