import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("figura tipo diamante")

#colores
colorFondo = pg.Color(255,255,255)
colorLinea = pg.Color(0,0,255)

pg.Surface.fill(screen, colorFondo)

centro = (400, 300)

#dibujar la figura
pg.draw.line(screen, colorLinea, (centro[0], 0), (centro[0], 600))
pg.draw.line(screen, colorLinea, (0, centro[1]), (800, centro[1]))

for i in range(0,400,10):
    pg.draw.line(screen, colorLinea, (centro[0], i), (centro[0]+i, centro[1]))

pg.display.flip()
input('Presiona enter para salir')
pg.quit()
    