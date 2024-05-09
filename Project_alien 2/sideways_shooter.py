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
        """initilize the game and create game resources"""
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display .set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.raindrops = pygame.sprite.Group()
        self.random_number = randint(-10, 10)
        
        self._create_fleet()
        self._create_storm()
        
    
        
    def run_game(self):
        '''starts the main loop for the game'''
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._update_rain()
            self._update_screen()
            self.clock.tick(60)
            #watch for keyboard and mouse events
        
            
    def _update_bullets(self):
        #get rid of bullets that have dissappeared 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))
            
         # Check for any bullets that have hit aliens.
        #   If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
            
    def _check_events(self):
        """Responds to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                    
    def _check_keydown_events(self, event):
        """responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
        
    def _check_keyup_events(self, event):
        """responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
            
            
    def _create_fleet(self):
        """create the fleet of aliens"""
        #create an alien and keep adding aliens until no room is left
        #make an alien
        #spacing between aliens is one alien is one alien width and one alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        self.aliens.add(alien)
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
                new_alien = Alien(self)
                new_alien.x = current_x
                new_alien.rect.x = current_x
                self.aliens.add(new_alien)
                #finished row; reset x value and increment y value
                current_x += 2 * alien_width
                current_y += 2 * alien_width
                
                for row in range(self.random_number):
                    for num in range(self.random_number):
                        x_position = randint(0, self.settings.screen_height - 3 * alien_height) + alien_width
                        y_position = randint(0, self.settings.screen_width - 2 * alien_width) + alien_height
                        self._create_alien(x_position, y_position)
                     
    def _create_rain(self):
        """makes steady rain while the game is running"""
        rain = Rain(self)
        rain_width, rain_height =  rain.rect.size
        self.rain.add(rain)
        
        current_x, current_y = rain_width, rain_height
        while current_y < (self.settings.screen_height - 3 * rain_height):
            while current_x < (self.settings.screen_width - 2 * rain_width):
                self._form_rain(current_x, current_y)
                current_x += 2 * rain_width
                new_rain = Alien(self)
                new_rain.x = current_x
                new_rain.rect.x = current_x
                self.rain.add(new_rain)
                #finished row; reset x value and increment y value
                current_x += 2 * rain_width
                current_y += 2 * rain_width
                
    def _create_storm(self):
        """create raindrops"""
        for _ in range(0,10):
            raindrop = Rain(self)  # Create a raindrop
            # Set random position within screen bounds
            raindrop.rect.x = randint(0, self.settings.screen_width - raindrop.rect.width)
            raindrop.rect.y = randint(-self.settings.screen_height, 0)
            self.raindrops.add(raindrop)  # Add raindrop to group
            
            
    def _form_rain(self, x_position, y_position):
        """create rain and places it in a row"""
        new_rain = Rain(self)
        new_rain.x = x_position
        new_rain.rect.x = x_position
        new_rain.rect.y = y_position
        self.rain.add(new_rain)
    
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        
    def _update_rain(self):
        """Update the position of raindrops"""
        self.raindrops.update()
        
        for raindrop in self.raindrops.sprites():
            if raindrop.rect.top >= self.settings.screen_height:
                self.raindrops.remove(raindrop)
        
       
        if len(self.raindrops) == 0:
            self._create_storm()  # Create a new row of raindrops
        
    def _update_screen(self):
        '''Updates images on the screen, and flip to new screen'''
        #redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()     
        self.aliens.draw(self.screen)  
        #draws the raindrops
        self.raindrops.draw(self.screen)
                    
        #Make the most recently drawn screen visible.
        pygame.display.flip()
            
                    
if __name__=='__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
                    