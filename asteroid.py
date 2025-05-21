import pygame
from circleshape import CircleShape
from constants import *
import random
# Asteroid class that inherits from CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid1.velocity = self.velocity.rotate(new_angle) * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid2.velocity = self.velocity.rotate(-new_angle) * 1.2