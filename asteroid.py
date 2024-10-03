import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 50
        else:
            split_angle = random.uniform(20, 50)

            first_angle = self.velocity.rotate(split_angle)
            second_angle = self.velocity.rotate(-split_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = first_angle * 1.2

            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = second_angle * 1.2

            return 100

