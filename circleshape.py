import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):     #Movement of all objects!
        # Add velocity to position (not replace)
        self.position +=self.velocity * dt

                
        # Wrap horizontally
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
            
        # Wrap vertically
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        

        
#check if there is collision and then adjust what to do depending on what the object is
    def collision(self, other_circle):
        r1 =self.radius
        r2 = other_circle.radius
        distance = pygame.Vector2.distance_to(self.position, other_circle.position)
        #print(distance)
        if(r1+r2>distance):
            return True
        else:
            return False
            