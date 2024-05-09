class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """initialize the game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (162,173,255)
        
        #Ship settings
        self.ship_speed = 1.5
        
        #Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.alien_frequency = 0.08
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        #raindrop settings
        self.fall_speed = 2.0
        
        
    
        
        
        
        
        