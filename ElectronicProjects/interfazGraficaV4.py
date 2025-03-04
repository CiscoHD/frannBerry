import pygame as pg
import gpiozero as gp 

import pygame as pg
import gpiozero as gz

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Interfaz Grafica")
clock = pg.time.Clock()

#Definir colores
bridgeColor = pg.Color(176,118,2)
borderBridgeColor = pg.Color(84,24,69)
borderButtonColor = pg.Color(122,122,122)
backColor = pg.Color(0,0,0)
upColor = pg.Color(0,255,0)
downColor = pg.Color(255,0,0)
ilustrationColor = pg.Color(0,200,255)
textColor = pg.Color(0,0,0)

running = True
fase = 0

#definirDimensiones
bridgeParts = (((100,50,60,200), (650, 50, 60, 200)), ((80,250, 100, 60), (630, 250, 100, 60)), ((50, 310, 160, 30 ), (600, 310, 160, 30)))  
bridgePlatform = (150,10 + 45*fase, 500, 20)
buttons = ((200, 450, 100, 100), (500, 450,100,100))
ilustrationDim = (0, 0, 800, 400)

#definirRectangulos
def rectMade():
    global bridgeSupports  (pg.Rect(bridgeParts[0][0]), pg.Rect(bridgeParts[0][1]))
    global bridgeBase  (pg.Rect(bridgeParts[1][0]), pg.Rect(bridgeParts[1][1]))
    global bridgePillars  (pg.Rect(bridgeParts[2][0]), pg.Rect(bridgeParts[2][1]))
    global upButton  pg.Rect(buttons[0])
    global downButton  pg.Rect(buttons[1])
    global ilustration  pg.Rect(ilustrationDim)

def printAll():
    pg.draw.rect(screen, ilustrationColor, ilustration, 0)
    pg.draw.rect(screen, bridgeColor, bridgeSupports[0], 0)
    pg.draw.rect(screen, borderBridgeColor, bridgeSupports[0], 2)
    pg.draw.rect(screen, bridgeColor, bridgeSupports[1], 0)
    pg.draw.rect(screen, borderBridgeColor, bridgeSupports[1], 2)
    pg.draw.rect(screen, bridgeColor, bridgeBase[0], 0)
    pg.draw.rect(screen, borderBridgeColor, bridgeBase[0], 2)
    pg.draw.rect(screen, bridgeColor, bridgeBase[1], 0)
    pg.draw.rect(screen, borderBridgeColor, bridgeBase[1], 2)
    pg.draw.rect(screen, bridgeColor, bridgePillars[0], 0)
    pg.draw.rect(screen, borderBridgeColor, bridgePillars[0], 2)
    pg.draw.rect(screen, bridgeColor, bridgePillars[1], 0)
    pg.draw.rect(screen, borderBridgeColor, bridgePillars[1], 2)
    pg.draw.rect(screen, upColor, upButton, 0)
    pg.draw.rect(screen, borderButtonColor, upButton, 2)
    pg.draw.rect(screen, downColor, downButton, 0)
    pg.draw.rect(screen, borderButtonColor, downButton, 2)

#while running:

pg.display.flip()

input('Press Enter to continue...')
pg.quit()