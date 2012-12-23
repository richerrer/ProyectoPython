import pygame
import Tkinter as tk
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
        sonido1 = pygame.mixer.Sound("parte00 Seleccion.wav")
        sonido2 = pygame.mixer.Sound("parte01 Seleccion.wav")
        canal.queue(sonido)
        canal.queue(sonido1)
        self.eleccionAcontecimiento(sonido,sonido1,"parte01.wav",canal)
        canal.queue(sonido2)
        self.eleccionAcontecimiento(sonido,sonido1,"parte01.wav",canal)
        
    def eleccionAcontecimiento(self,sonido,sonido1,titulo1,canal):
        verificador = False
        while not verificador:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1 :
                        self.detenerSonido(canal)
                        acontecimiento1 = pygame.mixer.Sound(titulo1)
                        canal.queue(acontecimiento1)
                        verificador = True
                        
    def detenerSonido(self,canal):
        sonido = canal.get_sound()
        if sonido != None:
            sonido.stop()
            
    def procesoDelCuento(self):
        i=0
        while True:
            if(i==0):
                self.iniciarCuento() 
                i=i+1
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    exit()          
               
                