import gpiod
import time

CHIP = "gpiochip0"
control_pins = (17, 18, 22, 23)

halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1],
]

chip = gpiod.Chip(CHIP)
lines = chip.get_lines(control_pins)

lines.request(consumer = "step_motor", type = gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        for halfstep in halfstep_seq:
            lines.set_values(halfstep)
            time.sleep(0.001)
        
        '''for halfstep in reversed(halfstep_seq):
            lines.set_values(halfstep)
            time.sleep(0.001)'''
except KeyboardInterrupt:
    print("estás imbécil")
finally:
    lines.release()
    chip.close()