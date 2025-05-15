import pygame
from circleshape import CircleShape
import constants as c
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, group_shots):
        super().__init__(x,y, c.PLAYER_RADIUS)
        self.rotation=0
        self.drag =0.95
        self.shots_group = group_shots
        self.time_since_last_shot=0
        self.score = 0
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
            self.rotation += c.PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation -= c.PLAYER_TURN_SPEED * dt
       
        # Keep rotation between 0-360
        self.rotation = self.rotation % 360
        
        # Calculate forward direction based on rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Set velocity based on keys pressed
        #self.velocity = pygame.Vector2(0, 0)  # Reset velocity
        if keys[pygame.K_w]:
            self.velocity += forward * c.PLAYER_SPEED* c.PLAYER_ACCELERATION*dt
        if keys[pygame.K_s]:
            #self.velocity = forward * -c.PLAYER_SPEED* c.PLAYER_ACCELERATION*dt
            if(self.velocity.length()>0.2)or not (self.velocity==0):
                self.velocity *= 0.95
            else:
                self.velocity=0
        if self.velocity.length() > c.MAX_PLAYER_SPEED:
            self.velocity = self.velocity.normalize() * c.MAX_PLAYER_SPEED

        #this timer will say when you can shoot again
        self.time_since_last_shot += dt        
        if keys[pygame.K_SPACE]:
            #self.shootcooldown = 0.25
            #self.time_since_last_shot=0
            if(self.time_since_last_shot >= c.SHOT_COOLDOWN):
                self.shoot()
                self.time_since_last_shot = 0 


        # Apply drag/friction to gradually slow down
        self.velocity *= self.drag



        

    def update(self, dt):
        # Handle input first
        self.handle_input(dt)
        
        # Let the parent class handle movement and wrapping
        super().update(dt)
        
        
    def collision(slef, other_circle):
        alive=super().collision(other_circle)

        if (alive):
            print("You have hit an Asteroid")
            raise SystemExit("you have died")

    def shoot(self):
        direction= self.rotation
        
        if(len(self.shots_group)>c.MAX_SHOTS):
            oldest_bullet = min(self.shots_group, key=lambda shot: shot.creationtime)
            oldest_bullet.kill()

        my_shot = Shot(self.position.x, self.position.y, direction, pygame.time.get_ticks())
        self.shots_group.add(my_shot)    
        


