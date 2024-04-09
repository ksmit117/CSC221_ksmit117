import sys
import pygame
from enemy import Enemy
from bullet import Bullet
from Assignment_settings import Settings
from Assignment12_ship import Ship



class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bg_color = (173,216,230)
        self.enemy = Enemy(self)

        self.enemies = pygame.sprite.Group()
     
        
        
        
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self.enemies.update()
            self._update_screen()
            self.clock.tick(60)
            
            
            
        
    def _check_keydown(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:  # Check if spacebar is pressed
            self._fire_bullet()  # Call _fire_bullet method when spacebar is pressed
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
            
    
    def _fire_bullet(self):
        """Fire a bullet if limit not reached yet."""
        new_bullet = Bullet(self)
        


    def update_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 


    def _update_screen(self):
        self.screen.fill(self.bg_color) 
        self.ship.blitme()
        self.enemies.draw(self.screen)
        
        pygame.display.flip()
        


        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)  # Call _check_keydown with the event
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)  # You also need to handle key releases

                
    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN: 
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
    
    
    
                    
    

                
                    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
   
                
                
