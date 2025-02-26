import gpiod
import time

CHIP = "gpiochip0"

# Definir pines
ENABLE_A = 12  # PWM Motor 1
ENABLE_B = 13  # PWM Motor 2
IN1 = 17  # Dirección Motor 1
IN2 = 18  # Dirección Motor 1
IN3 = 22  # Dirección Motor 2
IN4 = 23  # Dirección Motor 2

# Configurar pines GPIO
chip = gpiod.Chip(CHIP)
lines = chip.get_lines([ENABLE_A, ENABLE_B, IN1, IN2, IN3, IN4])
lines.request(consumer="DC_motor", type=gpiod.LINE_REQ_DIR_OUT)

# Configurar software PWM
PWM_FREQUENCY = 1000  # Frecuencia de la señal PWM en Hz
duty_cycle = 100 # % de potencia inicial

def set_motor_speed(enable_pin, speed):
    """Controla la velocidad del motor usando PWM."""
    period = 1.0 / PWM_FREQUENCY  # Tiempo total de un ciclo PWM
    high_time = (speed / 100.0) * period  # Tiempo en alto
    low_time = period - high_time  # Tiempo en bajo
    
    for _ in range(100):  # Ejecutar PWM manualmente (ajustable)
        lines.set_values([1 if enable_pin == ENABLE_A else 0,  # Enable A
                          1 if enable_pin == ENABLE_B else 0,  # Enable B
                          1, 0, 1, 0])  # Direcciones activas
        time.sleep(high_time)
        lines.set_values([0, 0, 1, 0, 1, 0])  # Apagar Enable temporalmente
        time.sleep(low_time)

try:
    while True:
        speed = int(input("Introduce la velocidad (0-100): "))
        if 0 <= speed <= 100:
            set_motor_speed(ENABLE_A, speed)
            set_motor_speed(ENABLE_B, speed)
        else:
            print("Valor fuera de rango.")

except KeyboardInterrupt:
    print("\nApagando motores...")
finally:
    lines.release()
    chip.close()
