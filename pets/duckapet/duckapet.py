import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time

pygame.init()

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

lakeBackground = displayio.OnDiskBitmap("lakeBackground.bmp")
bgSprite = displayio.TileGrid(lakeBackground, pixel_shader=lakeBackground.pixel_shader)
splash.append(bgSprite)

duckIdleSheet = displayio.OnDiskBitmap("duckIdle.bmp")
duckWalkSheet = displayio.OnDiskBitmap("duckWalk.bmp")

tileWidth = 32
tileHeight = 32

duckSprite = displayio.TileGrid(
    duckIdleSheet,
    pixel_shader=duckIdleSheet.pixel_shader,
    width=1,
    height=1,
    tile_width=tileWidth,
    tile_height=tileHeight,
    default_tile=0,
    x=(display.width - tileWidth) // 2,  
    y=display.height - tileHeight - 10     
)

splash.append(duckSprite)

frame = 0
speed = 2
delay = 5
nbParts = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()

    isMoving = False
    if keys[pygame.K_LEFT]:
        isMoving = True
        duckSprite.x -= speed
    if keys[pygame.K_RIGHT]:
        isMoving = True
        duckSprite.x += speed
    if keys[pygame.K_UP]:
        isMoving = True
        duckSprite.y -= speed
    if keys[pygame.K_DOWN]:
        isMoving = True
        duckSprite.y += speed
    
    if isMoving:
        currentDuckSheet = duckWalkSheet
    else:
        currentDuckSheet = duckIdleSheet
    
    duckSprite.bitmap = currentDuckSheet
    duckSprite[0] = frame // delay
    frame = (frame + 1) % (nbParts * delay)

    time.sleep(0.05)
