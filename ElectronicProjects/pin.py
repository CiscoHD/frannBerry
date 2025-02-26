from gpiozero import Button

button = Button(7)  # GPIO7
print("GPIO7 state:", button.is_pressed)
