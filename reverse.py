import pygame
import math
import random

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)
    def to_tuple(self):
        return (self.x, self.y)
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def normalize(self, new_magnitude):
        current_magnitude = self.get_magnitude()
        magnitude_ratio = new_magnitude / current_magnitude
        return self * magnitude_ratio


class Dot:
    def __init__(self, position, velocity):
        self.position = Vector2(position[0], position[1])
        self.velocity = Vector2(velocity[0], velocity[1])
    def move(self, dots):
        self.velocity += self.calculate_wall_acceleration_vector()
        for dot in dots:
            if dot != self:
                self.velocity += self.calculate_dot_acceleration_vector(dot)
        self.position += self.velocity
    def draw(self, display):
        pygame.draw.circle(display, (0, 0, 0), self.position.to_tuple(), 5)
    def calculate_dot_acceleration_vector(self, dot):
        s = 1
        direction = self.position - dot.position
        magnitude = direction.get_magnitude()
        force_magnitude = s / (magnitude ** 2)
        return direction.normalize(force_magnitude)
    def calculate_wall_acceleration_vector(self):
        s = 1
        x = s / (self.position.x ** 2) - s / ((800 - self.position.x) ** 2)
        y = s / (self.position.y ** 2) - s / ((800 - self.position.y) ** 2)
        return Vector2(x, y)

def main():
    pygame.init()
    pygame.display.set_caption("Anti-Gravity")
    screen = pygame.display.set_mode((800, 800))

    screen.fill((255, 255, 255))
    pygame.display.flip()

    dots = []
    for i in range(50):
        dots.append(Dot((random.random() * 800, random.random() * 800), (0, 0)))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))

        for dot in dots:
            dot.move(dots)
            dot.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
