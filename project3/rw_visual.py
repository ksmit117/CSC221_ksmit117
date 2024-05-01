import matplotlib.pyplot as plt
plt.style.available
from random import choice

class RandomWalk:
    """A class to generate random walks"""
    def __init__(self, num_points=5000):
        """"initialize the atributes of a walk"""
        self.num_points = num_points

        # all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]
        
    def get_step(self):
        direction = choice ([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
        
    def fill_walk(self):
        """calculate all the points in the walk"""
        #keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            x_direction = choice ([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = self.get_step()
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = self.get_step()
            
            # rejects moves to go nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            #calc new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
            

        
            
                