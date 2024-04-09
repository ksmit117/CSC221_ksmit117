import sys
import pygame
from bullet import Bullet
from Assignment_settings import Settings
from Assignment12_ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        # Swap width and height for landscape orientation
        self.screen = pygame.display.set_mode((1200, 800))  
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        # Rotate the ship sprite
        self.ship = Ship(self)
        self.ship.image = pygame.transform.rotate(self.ship.image, -90)
        self.ship.rect = self.ship.image.get_rect()
        self.ship.rect.midleft = (0, self.settings.screen_height // 2)
        
        self.bullets = pygame.sprite.Group()
        self.bg_color = (173, 216, 230)
        
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.update_bullets()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_keydown(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_LEFT:  # Change movement keys
            self.ship.moving_up = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_down = True
            
    def _fire_bullet(self):
        """Fire a bullet if limit not reached yet."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

    def _update_screen(self):
        self.screen.fill(self.bg_color) 
        # Draw ship rotated
        self.screen.blit(self.ship.image, self.ship.rect)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        pygame.display.flip()
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
