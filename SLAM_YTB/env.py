#Importar as bibliotecas
import math
import pygame

#Carrega o mapa e escalona a imagem de forma correta
class buildEnvironment:
    def __init__(self,MapDimensions):
        pygame.init()
        self.pointCloud=[]
        self.externalMap=pygame.image.load('PlantaIFSP-Model.png')
        self.maph, self.mapw = MapDimensions
        self.externalMap=pygame.transform.scale(self.externalMap,(self.mapw,self.maph))
        self.MapWindowName = 'RRT path planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        self.map.blit(self.externalMap, (0,0))

        #Cores
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)
        
    #Método que converte dados de distância em coordenadas cartesianas
    def AD2pos(self, distance, angle, robotPosition):
        x = distance * math.cos(angle)+robotPosition[0]
        y = -distance * math.sin(angle)+robotPosition[1]
        return (int(x), int(y))
    
    #Utiliza os dados AD2pos para verificar pontos duplicados
    def dataStorage(self, data):
        print(len(self.pointCloud))
        if data != False:
            for element in data:
                point = self.AD2pos(element[0], element[1], element[2])
                if point not in self.pointCloud:
                    self.pointCloud.append(point)
                    
    #Mostrar o mapa desenhado
    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])), self.Red)