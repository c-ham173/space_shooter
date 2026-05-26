import pygame
import sys
from logger import log_state
from logger import log_event
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0.0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
        
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

# GAME LOOP BEGIN
    while True:  # GAME LOOP
        
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
             for shot in shots:
                  if asteroid.collides_with(shot):
                       asteroid.split()
                       shot.kill()
                       log_event("asteroid_shot")
        
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        log_state()
    
# GAME LOOP END

if __name__ == "__main__":
    main()
