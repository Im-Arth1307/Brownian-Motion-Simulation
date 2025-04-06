import numpy as np # type: ignore
import random
import time

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
        """Check if the robot hits a boundary and adjust its position."""
        collision = False

        if self.x <= 0 or self.x >= WIDTH:
            self.x = max(1, min(WIDTH - 1, self.x))  # Keep in bounds
            collision = True

        if self.y <= 0 or self.y >= HEIGHT:
            self.y = max(1, min(HEIGHT - 1, self.y))
            collision = True

        if collision:
            # Move slightly backward before rotating to avoid getting stuck
            self.x -= self.speed * np.cos(np.radians(self.angle))
            self.y -= self.speed * np.sin(np.radians(self.angle))

            # Rotate by a random amount (30° - 150°) for natural movement
            self.angle += random.uniform(30, 150)
            self.angle %= 360  # Keep within 0-360 degrees

# Testing the robot movement (Remove this part in the final module)
if __name__ == "__main__":
    robot = Robot()
    for _ in range(100):
        robot.move_forward()
        robot.check_collision()
        print(f"Position: ({robot.x:.2f}, {robot.y:.2f}), Angle: {robot.angle:.2f}")
