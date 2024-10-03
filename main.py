import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    dt = 0

    player_score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        for object in updatable:
            object.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                print(f"Player Score: {player_score} !!!")
                if player_score == 0:
                    print("Rank: Dishonorably Discharged!!!")
                elif player_score <= 2500:
                    print("Rank: Mate")
                elif player_score <= 10000:
                    print("Rank: Lieutenant")
                elif player_score <= 25000:
                    print("Rank: Commander")
                elif player_score <= 50000:
                    print("Rank: Captain")
                elif player_score <= 75000:
                    print("Rank: Commodore")
                elif player_score <= 100000:
                    print("Rank: Rear Admiral")
                elif player_score <= 150000:
                    print("Rank: Vice Admiral")
                elif player_score <= 300000:
                    print("Rank: Admiral")
                elif player_score <= 500000:
                    print("Rank: Admiral of the Fleet")
                elif player_score <= 1000000:
                    print("Rank: 1st Space Lord")
                    print("Congratulations, you've mastered the game... maybe go play outside now?")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    player_score += asteroid.split()
                    shot.kill()


        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()