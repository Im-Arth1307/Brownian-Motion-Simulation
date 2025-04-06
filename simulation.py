import matplotlib.pyplot as plt # type: ignore
import matplotlib.animation as animation 
from brownian_motion import Robot

# Define arena size
WIDTH, HEIGHT = 500, 500

# Initialize Robot
robot = Robot()

# Set up Matplotlib figure
fig, ax = plt.subplots()
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)

ax.plot([0, WIDTH, WIDTH, 0, 0], [0, 0, HEIGHT, HEIGHT, 0], 'k-', linewidth=2)

point, = ax.plot([], [], 'ro', markersize=5)  # Robot represented as a red dot

def update(frame):
    """Update the robot's position in each frame."""
    robot.move_forward()
    robot.check_collision()
    point.set_data([robot.x], [robot.y])  # Wrap in a list
    return point,


# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show animation
plt.show()
