import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
            pass    

    def update(self, screen):
            pass

    def colliding(self, shape):
            r_sum = self.radius + shape.radius
            distance = self.position.distance_to(shape.position)
            return distance < r_sum
