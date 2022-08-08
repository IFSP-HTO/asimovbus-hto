import env, sensors
import pygame 
import math

enviroment = env.buildEnviroment((600, 1200))
running = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    