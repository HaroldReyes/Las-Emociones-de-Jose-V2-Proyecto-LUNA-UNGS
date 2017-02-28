import pygame
import EscenaHome  
import ClassDirector

def main():
    dir = ClassDirector.ClassDirector()
    scene = EscenaHome.EscenaHome(dir)
    dir.change_scene(scene)
    dir.loop()
 
if __name__ == '__main__':
    pygame.init()
    main()