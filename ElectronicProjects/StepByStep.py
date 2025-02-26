import gpiod
import time

CHIP = "gpiochip0"
control_pins = (17, 18, 22, 23)

# Secuencia de medio paso para máxima velocidad
step_seq = [
    [1, 0, 0, 0],  
    [1, 1, 0, 0],  
    [0, 1, 0, 0],  
    [0, 1, 1, 0],  
    [0, 0, 1, 0],  
    [0, 0, 1, 1],  
    [0, 0, 0, 1],  
    [1, 0, 0, 1],  
]

chip = gpiod.Chip(CHIP)
lines = chip.get_lines(control_pins)

lines.request(consumer="step_motor", type=gpiod.LINE_REQ_DIR_OUT)

# Función para mover el motor con máxima velocidad
def move_motor(steps, direction=1, delay=0.0015):  # Delay súper bajo para máxima rapidez
    """ Mueve el motor 'steps' en la dirección indicada (1 = CW, -1 = CCW) """
    sequence = step_seq if direction == 1 else list(reversed(step_seq))

    for _ in range(steps):
        for step in sequence:
            lines.set_values(step)
            time.sleep(delay)  # Delay mínimo para velocidad máxima

try:
    while True:
        move_motor(1024, 1, 0.0015)  # 1024 pasos (2 vueltas) ultra rápido
        move_motor(1024, -1, 0.0015)  # Gira en sentido contrario inmediatamente

except KeyboardInterrupt:
    print("\nMovimiento detenido.")
finally:
    lines.release()
    chip.close()

