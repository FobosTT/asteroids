from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.center = (x, y)
        self.radius = radius

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.center,
                           self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
