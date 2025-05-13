import pygame
from circleshape import CircleShape
#from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)


    def draw(self, screen):
        #pygame.draw.polygon(screen, "white", pygame.draw.circle(),2)
        pygame.draw.circle(screen, "white",self.position,self.radius ,2)

    def update(self, dt):
        #parent takes care of movement
        super().update(dt)

    def colide(player):
        pass
        