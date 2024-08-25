import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from astrofield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers for sprites
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    dt = 0
    time_clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    



    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")

    
        for drawes in drawable:
            drawes.draw(screen)

        pygame.display.flip()

        dt = time_clock.tick(60) / 1000
        for updates in updatable:
            updates.update(dt)

        for obj in asteroids:
            if obj.colliding(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if obj.colliding(bullet):
                    obj.split()
                    bullet.kill()


if __name__ == "__main__":
    main()