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
    
    def proceso_de_eleccion(self,canal):   
        if self.eleccionAcontecimiento("atajo.wav","rodear_la_montana.wav","opcion_atajo.wav","opcion_rodear_montana.wav",canal)==1:
            #ATAJO
            if self.eleccionAcontecimiento("rodear_la_montana.wav","investigar_de_donde_vino_el_sonido.wav","opcion_rodear_montana.wav","opcion_de_investigar_de_donde_vino_el_sonido.wav",canal)==1:
                #RODEAR MONTANA
                self.eleccionAcontecimiento("cruza_el_rio.wav","atraviesa_el_puente.wav","opcion_rodear_montana.wav","opcion_de_investigar_de_donde_vino_el_sonido.wav",canal)
            else :
                #INVESTIGAR DE DONDE VINO EL SONIDO
                self.ramas_de_conclusion(canal)
        else :
            #RODEAR MONTANA
            self.eleccionAcontecimiento("cruza_el_rio.wav","atraviesa_el_puente.wav","no existe opciones","no existe opciones",canal)
    
    
    def ramas_de_conclusion(self,canal):
        if self.eleccionAcontecimiento("entrar_a_la_nave.wav","salir_huyendo.wav","opciones_de_entrar_a_la_nave.wav","opciones_de_salir_huyendo.wav",canal)==1:
            #ENTRAR A LA NAVE
            if self.eleccionAcontecimiento("huir.wav","quedarse_acostado.wav","opciones_de_huir.wav","opciones_de_quedarse_acostado.wav",canal)==1:
                #HUIR
                self.eleccionAcontecimiento("letrero_naranja.wav","letrero_verde.wav","no existe opciones","no existe opciones",canal)        
            else:
                #QUEDARSE ACOSTADO
                self.eleccionAcontecimiento("golpear_al_alien.wav","letrero_verde.wav","no existe opciones","no existe opciones",canal)        
        else:
            #SALIR HUYENDO
            self.eleccionAcontecimiento("atravesar_el_pantano.wav","subir_la_escalera.wav","no existe opciones","no existe opciones",canal)            
        
    
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
               
                