from ClassEscena import*
from Helpers_Functions import*
from Helper_GIFImage import*
import pygame

class EscenaHome(ClassScene):
    def __init__(self, director):
        ClassScene.__init__(self, director)
    #===========================
    def on_event(self): 
        pass
    #===========================
    def on_update(self): 
        pass
    #===========================
    def on_draw(self, screen):
        screen.fill((255,255,255))
        Moon = GIFImage("Gif/Moon.gif")
        Moon.render(screen, (0, 0))
    #===========================