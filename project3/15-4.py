import matplotlib.pyplot as plt

from rw_visual import RandomWalk

  # Keep making new walks, as long as the program is active.
while True:
    rw = RandomWalk(50_00) 
    rw.fill_walk()

    #Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
   
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=30) 
    ax.set_aspect('equal')

   # Emphasize the first and last points.


    plt.show()
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[5], rw.y_values[8], c='red', edgecolors='none',
    s=100)
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break