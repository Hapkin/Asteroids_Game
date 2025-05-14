import pygame
import constants
from circleshape import *





class Shot(CircleShape):
    def __init__(self, x, y, direction, creationtime):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        velocity = pygame.Vector2(0, 1)
        velocity = velocity.rotate(direction)
        self.velocity = velocity * PLAYER_SHOOT_SPEED  # Scale it up
        self.direction = direction
        self.creationtime=creationtime

    def draw(self, screen):
        pygame.draw.circle(screen, "green",self.position,self.radius)


    def collision(self, asteroid):
        hit_asteroid=super().collision(asteroid)

        if(hit_asteroid):
            asteroid.kill()
            self.kill()