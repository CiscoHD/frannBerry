from gpiozero import Servo
from time import sleep

# Configuración del servomotor en GPIO 17
servo = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

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
        input("Presiona ENTER para abrir la pluma...")
        abrir_pluma()
        
        input("Presiona ENTER para cerrar la pluma...")
        cerrar_pluma()

except KeyboardInterrupt:
    print("\nPrograma finalizado.")
    servo.value = None  # Apagar el servo
