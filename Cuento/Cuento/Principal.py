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
        sonido = pygame.mixer.Sound("inicio.wav")
        opcion1 = pygame.mixer.Sound("opcion1.wav")
        canal.queue(sonido)
        canal.queue(opcion1)
        self.proceso_de_eleccion(canal)

    
    
    def eleccionAcontecimiento(self,titulo1,titulo2,opcion_acontesimiento1,opcion_acontesimiento2,canal):
        verificador = False
        while not verificador:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1 :
                        self.detenerSonido(canal)
                        acontecimiento1 = pygame.mixer.Sound(titulo1)
                        canal.queue(acontecimiento1)
                        self.verificar_existencia_opciones(opcion_acontesimiento1, canal)
                        verificador = True
                        r=1
                       
                    if evento.key == pygame.K_2 :
                        self.detenerSonido(canal)
                        acontecimiento2 = pygame.mixer.Sound(titulo2)
                        canal.queue(acontecimiento2)
                        self.verificar_existencia_opciones(opcion_acontesimiento2, canal)
                        verificador = True
                        r = 2
        return r
                
    def verificar_existencia_opciones(self,opcion_acontesimiento,canal):
        if opcion_acontesimiento!="no existe opciones":
            opcion = pygame.mixer.Sound(opcion_acontesimiento)
            canal.queue(opcion)           
            
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
               
                