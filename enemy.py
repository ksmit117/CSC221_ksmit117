import pygame

class Enemy:
    '''class that manages the ship'''
    
    # Inside Enemy class __init__ method
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # Load the image for the enemy ship
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        
        # Position the enemy ship at the center of the screen's top
        self.rect.midtop = self.screen_rect.midtop

