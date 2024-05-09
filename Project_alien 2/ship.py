import pygame

class Ship:
    """A class to mange the ship"""
    
    def __init__(self, ai_game):
        """initialize the ship and set its varitent"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load the ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom center of the screen
        self.rect.center = self.screen_rect.center
        
        #Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)
        
        
        #Movement flag; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        
    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
            
        #update rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the ship at its current location"""
        rotated_image = pygame.transform.rotate(self.image, 90)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        self.screen.blit(rotated_image, rotated_rect)