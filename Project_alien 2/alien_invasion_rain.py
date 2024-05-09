import sys
import pygame
from random import randint
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from rain import Rain

class AlienInvasion:
    """Overall a class to manage the game asset and behavior"""
    def __init__(self):
        """initialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.rain = pygame.sprite.Group()  # Group for raindrops
        self.random_number = randint(-10, 10)
        
        self._create_fleet()
        self._create_storm()  # Create the initial raindrops
        
    def run_game(self):
        '''starts the main loop for the game'''
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._update_rain()  # Update raindrops
            self._update_screen()
            self.clock.tick(60)
    
    def _update_rain(self):
        """Update the position of raindrops"""
        self.rain.update()
        
        # Remove raindrops that have gone off the screen
        for raindrop in self.rain.copy():
            if raindrop.rect.top >= self.settings.screen_height:
                self.rain.remove(raindrop)
        
        # Create a new row of raindrops if needed
        if len(self.rain) == 0:
            self._create_storm()
        
    def _create_storm(self):
        """Create a new row of raindrops"""
        for _ in range(10):  # Number of raindrops in a row
            raindrop = Rain(self)  # Create a raindrop
            self.rain.add(raindrop)  # Add it to the rain group
            
    def _check_events(self):
        """Responds to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """responds to keypresses"""
        if event.key == pygame.K_q:
            sys.exit()
    
    def _update_bullets(self):
        # get rid of bullets that have disappeared 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _create_fleet(self):
        """create the fleet of aliens"""
        # Your code for creating the fleet goes here
    
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        # Your code for updating aliens goes here
    
    def _update_screen(self):
        '''Updates images on the screen, and flip to new screen'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()     
        self.aliens.draw(self.screen)
        self.rain.draw(self.screen)  # Draw raindrops
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
