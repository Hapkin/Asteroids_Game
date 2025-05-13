import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
        self.drag =0.95
        #print(f"the player is created. position: {x},{y}")
        


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        #print(f"{a},{b},{c}")
        return [a, b, c]


    #from https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
    #    pygame.draw.polygon(screen, "black", [[100, 100], [0, 200], [200, 200]], 5)

    def draw(self, screen):
        #pygame.draw.circle(screen, "blue", (int(self.position.x), int(self.position.y)), self.radius)
        pygame.draw.polygon(screen, "white", self.triangle(),2)
        #Sprint(f"Drawing triangle{self.triangle()}")
    
    def handle_input(self, dt):
        keys = pygame.key.get_pressed()
        
        # Turn left/right
        if keys[pygame.K_a]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation -= PLAYER_TURN_SPEED * dt
       
        # Keep rotation between 0-360
        self.rotation = self.rotation % 360
        
        # Calculate forward direction based on rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Set velocity based on keys pressed
        #self.velocity = pygame.Vector2(0, 0)  # Reset velocity
        if keys[pygame.K_w]:
            self.velocity += forward * PLAYER_SPEED* PLAYER_ACCELERATION*dt
        if keys[pygame.K_s]:
            #self.velocity = forward * -PLAYER_SPEED* PLAYER_ACCELERATION*dt
            if(self.velocity.length()>0.2):
                self.velocity *= 0.95
            else:
                self.velocity=0
        if self.velocity.length() > MAX_PLAYER_SPEED:
            self.velocity = self.velocity.normalize() * MAX_PLAYER_SPEED
        #print(f"{self.position}")

        # Apply drag/friction to gradually slow down
        self.velocity *= self.drag



        

    def update(self, dt):
        # Handle input first
        self.handle_input(dt)
        
        # Let the parent class handle movement and wrapping
        super().update(dt)
        
        




