import gpiozero as gpio
from time import sleep

# Configuración de pines
output1 = gpio.DigitalOutputDevice(14)  # Dirección motor 1
output2 = gpio.DigitalOutputDevice(15)  # Dirección motor 2
enable1 = gpio.PWMOutputDevice(18)  # Habilitación motor 1 (PWM)
enable2 = gpio.PWMOutputDevice(13)  # Habilitación motor 2 (PWM)
servo = gpio.Servo(23, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)  # Control de pluma

# Sensores de límite (botones)
up_arrived = gpio.Button(2, pull_up=True)
down_arrived = gpio.Button(3, pull_up=True)

def menu():
    print("\n----- Puente de elevación -------")
    print("w) Subir plataforma")
    print("s) Bajar plataforma")
    print("q) Parar motores")
    print("e) Salir")
    return input("Ingresa una opción: ").lower()

def elevar_plataforma():
    """Sube la plataforma hasta que el botón superior lo detenga."""
    if up_arrived.is_pressed:
        print("⚠️ La plataforma ya está arriba")
        return
    
    print("⏫ Elevando plataforma...")
    enable1.value = 1
    enable2.value = 1
    output1.on()
    output2.off()

def bajar_plataforma():
    """Baja la plataforma hasta que el botón inferior lo detenga."""
    if down_arrived.is_pressed:
        print("⚠️ La plataforma ya está abajo")
        return
    
    print("⏬ Bajando plataforma...")
    enable1.value = 1
    enable2.value = 1
    output1.off()
    output2.on()

def detener_motores():
    """Apaga los motores."""
    print("🛑 Motores detenidos")
    enable1.value = 0
    enable2.value = 0
    output1.off()
    output2.off()

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

# Detectar si la plataforma llegó al tope
def detectar_limites():
    if up_arrived.is_pressed:
        print("✅ Plataforma arriba")
        detener_motores()
    
    if down_arrived.is_pressed:
        print("✅ Plataforma abajo, abriendo pluma...")
        detener_motores()
        abrir_pluma()

abrir_pluma()

try:
    while True:
        opcion = menu()
        
        if opcion == 'w':
            elevar_plataforma()
            cerrar_pluma()
        elif opcion == 's':
            bajar_plataforma()
        elif opcion == 'q':
            detener_motores()
        elif opcion == 'e':
            break
        else:
            print("⚠️ Opción inválida, intenta de nuevo.")
        up_arrived.when_pressed = detectar_limites
        down_arrived.when_pressed = detectar_limites

except KeyboardInterrupt:
    print("\n🛑 Interrupción del usuario")

finally:
    print("🔻 Finalizando programa, apagando motores y cerrando pluma...")
    detener_motores()
    cerrar_pluma()
