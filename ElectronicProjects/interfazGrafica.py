import gpiozero as gpio
from time import sleep
import pygame as pg

pg.init()

'''
input1 = gpio.DigitalOutputDevice(14)
input2 = gpio.DigitalOutputDevice(15)
enable1 = gpio.PWMOutputDevice(18) #Motor1
enable2 = gpio.PWMOutputDevice(13) #Motor2

def foward():
    input1.on()
    input2.off()
    enable1.value = 0.9
    enable2.value = 1

def backward():
    input1.off()
    input2.on()
    enable1.value = 1
    enable2.value = 0.9
def stop():
    input1.off()
    input2.off()
    enable1.value = 0
    enable2.value = 0
'''
colorFondo = pg.Color(255,255,255)
colorBotonArriba = pg.Color(0,255,0)
colorBotonAbajo = pg.Color(255,0,0)
colorIlustracion = pg.Color(0,200,255)

yBut = 450
xBut = [200, 500]
alBut = 100
anBut = 100

botonAbajo = pg.Rect( xBut[0], yBut, anBut, alBut)
botonArriba = pg.Rect(xBut[1], yBut, anBut, alBut)
ilustracion = pg.Rect(0,0,800,400)

clock = pg.time.Clock()

pg.display.set_caption("Controlador de puente")
screen = pg.display.set_mode((800, 600))
running = True
pg.Surface.fill(screen, colorFondo)
font = pg.font.Font(None, 36)

i = 0
statusPuente = "Detenido"

pg.draw.rect(screen, colorBotonArriba, botonArriba, 0)
pg.draw.rect(screen, colorBotonAbajo, botonAbajo, 0)
pg.draw.rect(screen, colorIlustracion, ilustracion, 0)


while running == True:
    pg.display.flip()
    mousex, mousey = pg.mouse.get_pos()
    click = pg.mouse.get_pressed(num_buttons=5)
    if mousex > xBut[0] and mousex < xBut[0] + anBut and mousey > yBut and mousey < yBut + alBut:
        statusMouse = "bajada"
    elif mousex > xBut[1] and mousex < xBut[1] + anBut and mousey > yBut and mousey < yBut + alBut:
        statusMouse = "subida"
    else: 
        statusMouse = "noValid"

    key = pg.key.get_pressed()

    if (key[pg.K_w] or (statusMouse == "subida" and click == (1,0,0,0,0))) and statusPuente == "Detenido":
        varText = font.render("Arriba", True, (0,0,0))
        screen.blit(varText, (350,100))
        i = 0
        statusPuente = "Subiendo"
       # foward()
    elif (key[pg.K_s] or (statusMouse == "bajada" and click == (1,0,0,0,0))) and statusPuente == "Detenido":
        varText = font.render("Abajo", True, (0,0,0))
        screen.blit(varText, (350,100))
        i = 0
        statusPuente = "Bajando"
       # backward()
    elif key[pg.K_a] :
        varText = font.render("Detener", True, (0,0,0))
        '''screen.blit(varText, (350,100))
        #stop()'''
    elif i == 300:
        pg.Surface.fill(screen, colorFondo)
        #stop()
        statusPuente = "Detenido"
        pg.draw.rect(screen, colorBotonArriba, botonArriba, 0)
        pg.draw.rect(screen, colorBotonAbajo, botonAbajo, 0)
        pg.draw.rect(screen, colorIlustracion, ilustracion, 0)
    #Terminación de programa
    elif key[pg.K_d]:
        running = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(60)
    i += 1
pg.quit()