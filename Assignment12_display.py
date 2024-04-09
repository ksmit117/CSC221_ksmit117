import pygame
import sys

class Key_pressed:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Keys Demo")
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print("Key pressed:", event.key)
                    
            pygame.display.update()

    if __name__ == "__main__":
        __init__()

                    