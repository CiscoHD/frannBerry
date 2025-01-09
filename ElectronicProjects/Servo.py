import gpiod
import time

CHIP = "gpiochip0"
PIN = 4

MIN_DUTY_CYCLE = 3
MID_DUTY_CYCLE = 7
MAX_DUTY_CYCLE = 11

chip = gpiod.Chip(CHIP)
line = chip.get_line(PIN)

line.request(consumer = "servo_motor", type = gpiod.LINE_REQ_DIR_OUT)

def pwm_signal(duty_cycle):
    period = 0.01
    pulse_width = period * duty_cycle / 100

    while True:
        line.set_value(1)
        time.sleep(pulse_width)
        line.set_value(0)
        time.sleep(period - pulse_width)

def move_servo_to_angle(angle):
    if angle == 0:
        duty_cycle = MIN_DUTY_CYCLE
    elif angle == 90:
        duty_cycle = MID_DUTY_CYCLE
    elif angle == 180:
        duty_cycle = MAX_DUTY_CYCLE
    else:
        print("tas re menso no se puede ver desde ese angulo")

    print("Mover Servomotor a {} grados".format(angle))
    pwm_signal(duty_cycle)

i = 0 
try:
    while i <= 180:
        move_servo_to_angle(i)
        time.sleep(1)

        move_servo_to_angle(i)
        time.sleep(1)

        move_servo_to_angle(i)
        time.sleep(1)

        i += 90

except KeyboardInterrupt:
    print("todo pendejo")

finally:
    line.release()
    chip.close()



