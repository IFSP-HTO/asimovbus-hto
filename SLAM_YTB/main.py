#Importanto as bibliotecas e arquivos criados
import env, sensors
import pygame
import math
import keyboard

#Construção do ambiente
environment = env.buildEnvironment((600, 1200))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(200, environment.originalMap, uncertainty=(0.5, 0.01))
environment.map.fill((0, 0, 0))
environment.infomap = environment.map.copy()

running = True

while running:
    sensorON = False
    for event in pygame.event.get(): #O código só funcionará quando o mouse estiver na janela
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False
            
    #Enquanto estiver rodando, as posições do mouse serão registradas
    if sensorON:
        position = pygame.mouse.get_pos() #Registro dos pontos
        laser.position = position #Aderindo as posições ao sensor
        sensor_data = laser.sense_obstacles() #Detecção dos obstaculos com as posições dos pontos
        environment.dataStorage(sensor_data) #Armazena dados para mostrá-los
        environment.show_sensorData() #Desenha os pixels em vermelho na tela
    environment.map.blit(environment.infomap, (0, 0)) #Desenha por cima do mapa preto "infomap"
    pygame.display.update() #Atualiza o display
    
    #Caso pressione 'Esc', a janela fechará e encerra o loop
    if keyboard.is_pressed('Esc'):
        pygame.display.quit()
        break
