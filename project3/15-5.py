import matplotlib.pyplot as plt
from rw_visual import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    rw = RandomWalk() 
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))

    # Create a color map based on the number of points in the walk.
    colors = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=colors, cmap=plt.cm.Blues, edgecolors='none', s=30) 

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[0], rw.y_values[8], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #refactored in rw_visual.py
    plt.show()
  

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
      
      
      
