import pygame
import Home  
import Director

def main():
    
    dir = Director.Director()
    scene = Home.Home(dir)
    dir.change_scene(scene)
    dir.loop()
 
if __name__ == '__main__':
    pygame.init()
    main()