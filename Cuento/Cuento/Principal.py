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
        canal = pygame.mixer.Channel(2)
        
        sonido = pygame.mixer.Sound("parte00.wav")
        sonido2 = pygame.mixer.Sound("parte00 Seleccion.wav")
        sonido3 = pygame.mixer.Sound("parte01 Seleccion.wav")
        canal.queue(sonido)
        canal.queue(sonido2)
        sonido3.play()
        entrada = self.capturarEntrada()
        self.eleccionAcontecimiento(entrada, canal)
    
    def eleccionAcontecimiento(self,entrada,canal):
        if(entrada==1):
            s = canal.get_sound()#s es el sonido que se esta reproduciendo
            if s != None:
               s.stop()#se detiene el sonido
            sonido1 = pygame.mixer.Sound("parte01.wav")
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
