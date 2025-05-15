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

    
    def collision(self, other_circle):
        hit_asteroid=super().collision(other_circle)
        
        if(hit_asteroid):
            #print("Asteroid collision")
            
            direction = self.position - other_circle.position
            if direction.length() != 0:
                direction = direction.normalize()
                nudge = direction * 3  # nudge amount (3 can be adjusted)
                self.position += nudge
                other_circle.position -= nudge
            
            
            
            #set direction and new speed
            self.velocity = self.velocity.reflect(direction) * 0.90
            other_circle.velocity = other_circle.velocity.reflect(-direction) * 0.90
            
            if self.velocity.length() < ASTEROID_MIN_SPEED:
                self.velocity = self.velocity.normalize() * ASTEROID_MIN_SPEED
            if other_circle.velocity.length() < ASTEROID_MIN_SPEED:
                other_circle.velocity = other_circle.velocity.normalize() * ASTEROID_MIN_SPEED
        
        
            #current_velocity_self.velocity=pygame.Vector2(current_velocity_other.x,current_velocity_other.y)
            #current_velocity_other.velocity=pygame.Vector2(current_velocity_other.x,current_velocity_other.y)


        