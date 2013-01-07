import pygame
from pygame.locals import *
import os

def main():
    p=Principal()
    

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
        sonido = pygame.mixer.Sound(os.path.join("sonidos", "inicio.wav"))
        opcion1 = pygame.mixer.Sound(os.path.join("sonidos", "opcion1.wav"))
        canal.queue(sonido)
        canal.queue(opcion1)
        self.proceso_de_eleccion(canal)
    
    def proceso_de_eleccion(self,canal):   
        if self.eleccionAcontecimiento(os.path.join("sonidos", "atajo.wav"),os.path.join("sonidos", "rodear_la_montana.wav"),os.path.join("sonidos", "opcion_atajo.wav"),os.path.join("sonidos", "opcion_rodear_montana.wav"),canal)==1:
            #ATAJO
            if self.eleccionAcontecimiento(os.path.join("sonidos", "rodear_la_montana.wav"),os.path.join("sonidos", "investigar_de_donde_vino_el_sonido.wav"),os.path.join("sonidos", "opcion_rodear_montana.wav"),os.path.join("sonidos", "opcion_de_investigar_de_donde_vino_el_sonido.wav"),canal)==1:
                #RODEAR MONTANA
                self.ramas_de_rodear_montana(canal)
            else :
                #INVESTIGAR DE DONDE VINO EL SONIDO
                self.ramas_de_entrar_en_la_nave(canal)
        else :
            #RODEAR MONTANA
            self.ramas_de_rodear_montana(canal)
    
    def ramas_de_entrar_en_la_nave(self,canal): #UNA DE LAS RAMAS PRINCIPALES
        if self.eleccionAcontecimiento(os.path.join("sonidos", "entrar_a_la_nave.wav"),os.path.join("sonidos", "salir_huyendo.wav"),os.path.join("sonidos", "opciones_de_entrar_a_la_nave.wav"),os.path.join("sonidos", "opciones_de_salir_huyendo.wav"),canal)==1:
            #ENTRAR A LA NAVE
            if self.eleccionAcontecimiento(os.path.join("sonidos", "huir.wav"),os.path.join("sonidos", "quedarse_acostado.wav"),os.path.join("sonidos", "opciones_de_huir.wav"),os.path.join("sonidos", "opciones_de_quedarse_acostado.wav"),canal)==1:
                #HUIR
                self.eleccionAcontecimiento(os.path.join("sonidos", "letrero_naranja.wav"),os.path.join("sonidos", "letrero_verde.wav"),"no existe opciones","no existe opciones",canal)        
            else:
                #QUEDARSE ACOSTADO
                self.eleccionAcontecimiento(os.path.join("sonidos", "golpear_al_alien.wav"),os.path.join("sonidos", "letrero_verde.wav"),"no existe opciones","no existe opciones",canal)        
        else:
            #SALIR HUYENDO
            self.eleccionAcontecimiento(os.path.join("sonidos", "atravesar_el_pantano.wav"),os.path.join("sonidos", "subir_la_escalera.wav"),"no existe opciones","no existe opciones",canal)            
        
    
    def ramas_de_rodear_montana(self,canal):#OTRA DE LAS RAMAS PRINCIPALES QUE CONTIENE LA RAMA DE ENTRAR EN LA NAVE
        if self.eleccionAcontecimiento(os.path.join("sonidos", "cruza_el_rio.wav"),os.path.join("sonidos", "atraviesa_el_puente.wav"),os.path.join("sonidos", "opciones_de_cruzar_nadando.wav"),os.path.join("sonidos", "opciones_de_cruzar_puente.wav"),canal)==1:
            #CRUZAR EL RIO
            if self.eleccionAcontecimiento(os.path.join("sonidos", "lo_golpea_una_piedra.wav"),os.path.join("sonidos", "no_lo_golpea_una_piedra.wav"),os.path.join("sonidos", "opcion_de_investigar_de_donde_vino_el_sonido.wav"),os.path.join("sonidos", "opcion_de_investigar_de_donde_vino_el_sonido.wav"),canal)==1:
                #LO GOLPEA UNA PIEDRA
                self.ramas_de_entrar_en_la_nave(canal)
            else:
                #NO LO GOLPEA UNA PIEDRA
                self.ramas_de_entrar_en_la_nave(canal)
        else:
            #ATRAVIESA EL PUENTE
            if self.eleccionAcontecimiento(os.path.join("sonidos", "cruza_el_puente.wav"),os.path.join("sonidos", "cae_del_puente.wav"),os.path.join("sonidos", "opcion_de_investigar_de_donde_vino_el_sonido.wav"),os.path.join("sonidos", "opcion_de_investigar_de_donde_vino_el_sonido.wav"),canal)==1:
                #CRUZA EL PUENTE
                self.ramas_de_entrar_en_la_nave(canal)
            else:
                #CAE DEL PUENTE
                self.ramas_de_entrar_en_la_nave(canal)
        
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
                        
                if evento.type == pygame.QUIT:
                    exit()
            
                 
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



main()
                
