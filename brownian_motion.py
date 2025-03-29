import numpy as np
import random

# Define arena size
WIDTH, HEIGHT = 500, 500

class Robot:
    def __init__(self):
        """Initialize the robot in the center of the arena."""
        self.x = WIDTH // 2  # Start in the center
        self.y = HEIGHT // 2
        self.angle = random.uniform(0, 360)  # Random initial direction
        self.speed = 5  # Pixels per step

    def move_forward(self):
        """Move in the current direction."""
        self.x += self.speed * np.cos(np.radians(self.angle))
        self.y += self.speed * np.sin(np.radians(self.angle))

    def check_collision(self):
        """Check if the robot hits a boundary and reflect its direction."""
        if self.x <= 0 or self.x >= WIDTH:
            self.angle = 180 - self.angle  # Reflect horizontally
        if self.y <= 0 or self.y >= HEIGHT:
            self.angle = -self.angle  # Reflect vertically

# Testing the robot movement (Remove this part in the final module)
if __name__ == "__main__":
    robot = Robot()
    for _ in range(100):
        robot.move_forward()
        robot.check_collision()
        print(f"Position: ({robot.x:.2f}, {robot.y:.2f}), Angle: {robot.angle:.2f}")
