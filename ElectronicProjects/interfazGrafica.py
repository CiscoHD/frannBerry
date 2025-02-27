import gpiozero as gpio
from time import sleep
import pygame as pg

pg.init()

colorFondo = pg.Color(255,255,255)
colorBotonArriba = pg.Color(0,255,0)
colorBotonAbajo = pg.Color(255,0,0)
colorIlustracion = pg.Color(0,200,255)

botonAbajo = pg.Rect(200,450,100,100)
botonArriba = pg.Rect(500,450,100,100)
ilustracion = pg.Rect(0,0,800,400)

pg.display.set_caption("Controlador de puente")
screen = pg.display.set_mode((800, 600))
pg.Surface.fill(screen, colorFondo)


pg.draw.rect(screen, colorBotonArriba, botonArriba, 0)
pg.draw.rect(screen, colorBotonAbajo, botonAbajo, 0)
pg.draw.rect(screen, colorIlustracion, ilustracion, 0)

pg.display.flip()
input("Presione enter para continuar")


pg.quit()