from circleshape import CircleShape
from constants import *
import pygame
import random
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position,
                           self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20.0, 50.0)
        new_vec1 = self.velocity.rotate(angle)
        new_vec2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid1 = Asteroid(
            self.position.x, self.position.y, new_radius)
        split_asteroid2 = Asteroid(
            self.position.x, self.position.y, new_radius)
        split_asteroid1.velocity = new_vec1 * 1.2
        split_asteroid2.velocity = new_vec2 * 1.2
