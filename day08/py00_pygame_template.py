# py00_pygame_template.py

import pygame 
from pygame.locals import QUIT 
import sys   

pygame.init()
Surface = pygame.display.set_mode((640, 400))  
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Basic')

def main():
    while True:
        Surface.fill(color='black')     # Surface.fill((255, 255, 255))  
        for event in pygame.event.get(): 
            if event.type == QUIT:  
                pygame.quit()   
                sys.exit()      

        pygame.display.update() 
        FPSCLOCK.tick() 

if __name__ == '__main__':
    main()