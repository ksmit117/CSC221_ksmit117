import pygame 
class Ship:
    '''class that manages the ship'''
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        
        self.image = pygame.image.load('armored_skeleton_slash.gif')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.center
        
        self.x = float(self.rect.x)
        
        
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
            
    def update(self):
    # Update the ship's location based on movement flags
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

        # Update the rect object from self.x
        self.rect.x = int(self.x)


            
            
    def blitme(self):
        '''draws the ship at its current location'''
        self.screen.blit(self.image, self.rect)