import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


# This is the main game loop
# It initializes the game, creates a player object, and handles events
# It also updates the game state and draws the player on the screen

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        updateable.update(dt)
        if player.timer > 0:
            player.timer -= dt
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                pygame.quit()
                return
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
                    break
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()