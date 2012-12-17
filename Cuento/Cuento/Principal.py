import pygame
from pygame.locals import *

class Principal():
    
    def __init__(self):
        self.inicializarElementos()
        self.procesoDelCuento()
        
    def inicializarElementos(self):
        pygame.init() 
        pantalla = pygame.display.set_mode((470,300),0,32)
        pygame.display.set_caption("Historia")
        
    def iniciarCuento(self):
        sonido = pygame.mixer.Sound("parte00.wav")
        sonido.play()
        entrada = self.capturarEntrada()
        self.eleccionAcontecimiento(entrada, sonido)
    
    def eleccionAcontecimiento(self,entrada,sonido):
        if(entrada==1):
            sonido.stop()
            sonido1 = pygame.mixer.Sound("parte00.wav")
            sonido1.play()
    
    def capturarEntrada(self):
        entrada = int(input("digite"))
        return entrada
      
    def procesoDelCuento(self):
        i=0
        while True:
            if(i==0):
                self.iniciarCuento() 
                i=i+1
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    exit()