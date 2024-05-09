import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to mange bullets fired from the ship"""
    def __init__(self, ai_game):
        """create a bullet fired from the ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = ai_game.ship.rect.midleft
        
        #store the bullet's position as a float
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the bullet up the screen"""
        # Update the exact position of the bullet
        self.x -= self.settings.bullet_speed
        # Update the rect position
        self.rect.x = self.x

        
        

        
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)