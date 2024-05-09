import pygame
from random import randint

class Rain(pygame.sprite.Sprite):
    """A class for the rain"""
    
    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('raindrop.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = randint(-self.settings.screen_height, 0)
        self.fall_speed = self.settings.fall_speed
        
        # Set the initial position of the raindrop to the top of the screen
        self.rect.top = self.screen.get_rect().top
        
    def update(self):
        """Move the raindrop down."""
        self.rect.y += self.fall_speed
        
    def draw(self, screen):
        """Draw the raindrop on the screen."""
        screen.blit(self.image, self.rect)
