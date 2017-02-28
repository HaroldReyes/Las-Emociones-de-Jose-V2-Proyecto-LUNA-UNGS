import pygame
import sys
from ClassEscena import*
from Config import*

class ClassDirector: 
    def __init__(self):
        #============================================================
        #Nombre de proyecto
        #============================================================
        pygame.display.set_caption(NOMBREPROYECTO)
        #============================================================
        #Opciones de pantalla
        #============================================================
        if FULLSCREEN:
            self.screen = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)  
        else:
            self.screen = pygame.display.set_mode((ANCHO, ALTO))
        #============================================================     
        
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock() 
    #============================================================
    #Loop principal
    #============================================================     
    def loop(self):  
        while not self.quit_flag:
             
            time = self.clock.tick(FPS)
              
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Salir()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: 
                       Salir()
  
            self.scene.on_event() 
            self.scene.on_update() 
            self.scene.on_draw(self.screen)
            pygame.display.flip()
   #============================================================
    #Cambio de Escena
    #============================================================     
    def change_scene(self, scene): 
        self.scene = scene
    #============================================================     
     #Quitar escena
    #============================================================     
    def quit(self):
        self.quit_flag = True
    #============================================================     
#============================================================
#Salir de el juego
#============================================================     
def Salir():
    pygame.quit()
    quit()
#============================================================     