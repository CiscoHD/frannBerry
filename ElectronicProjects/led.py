import gpiod 
import time 

CHIP = "gpiochip0"
PIN = 4

chip = gpiod.Chip(CHIP)
line = chip.get_line(PIN)

line.request(consumer = "led-control", type = gpiod.LINE_REQ_DIR_OUT)

for i in range (50):
    if i % 2 == 0:
        line.set_value(1)
        print("LED encendido")

    time.sleep(.1)

    if i % 2 != 0:
        line.set_value(0)
        print("led apagado")
    time.sleep(.1)
line.release()
chip.close()