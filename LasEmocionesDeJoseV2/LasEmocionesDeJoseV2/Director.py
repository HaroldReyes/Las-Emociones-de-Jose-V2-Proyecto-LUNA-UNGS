import pygame
import sys
from Escena import*

class Director: 
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Nombre Proyecto")
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()
 
    def loop(self):  
        while not self.quit_flag:
            time = self.clock.tick(60)
              
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
 
    def change_scene(self, scene): 
        self.scene = scene
 
    def quit(self):
        self.quit_flag = True

def Salir():
    pygame.quit()
    quit()