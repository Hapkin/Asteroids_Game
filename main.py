## this allows us to use code from
# the open-source pygame library
# throughout this file
## imports outside
import pygame
import sys
import random
## imports from project
import constants as c
#from player import player => Classes Always Start Capitalized
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

#from circleshape import CircleShape



def main():
    try:
        print("Starting Asteroids!")
        print(f"Screen width: {c.SCREEN_WIDTH}")
        print(f"Screen height: {c.SCREEN_HEIGHT}")
        bg_image = pygame.image.load('black_space.jpg')

        pygame.init()
        
        
        clock=pygame.time.Clock()

        dt=0
        screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        
        pygame.display.set_caption('Keen in between worlds')
        
        x=(c.SCREEN_WIDTH/2)
        y =(c.SCREEN_HEIGHT/2)
        #create groups
        group_updatable = pygame.sprite.Group()
        group_drawable = pygame.sprite.Group()
        group_shots= pygame.sprite.Group()
        group_asteroids= pygame.sprite.Group()
        #create containers
        Player.containers = (group_updatable, group_drawable)
        Shot.containers = (group_shots, group_updatable, group_drawable)
        Asteroid.containers = (group_asteroids, group_updatable, group_drawable)
        AsteroidField.containers = (group_updatable,)
        
        
        

        #create items for the containers
        my_player= Player(x,y, group_shots)  # Will be used through groups
        my_asteroidfield =AsteroidField()
        
        

        #this happens behind the scenes of magical pygame framework
        #group_drawable.add(my_player)
        #group_updatable.add(my_player)

        #print(f"Is player a CircleShape? {isinstance(my_player, CircleShape)}")
        #print(f"Player position: {my_player.position.x}, {my_player.position.y}")
        #print(f"Screen dimensions: {c.SCREEN_WIDTH}, {c.SCREEN_HEIGHT}")
        #print(dir(my_player))
        

        while True:
            #### before we do anything check if exit is pressed ###
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #print(dt)
                    return
            ### end of exit
            

            #screen.fill("black")
            screen.blit(bg_image , (0,0))
            dt=clock.tick(60) /1000
            #score text
            font = pygame.font.Font(None, 36)
            


            ##first we just drew the player -> later we updated to draw every object in the groups
            #my_player.draw(screen)
            #my_player.update(dt)
            #print(f"Triangle points: {my_player.triangle()}")

            
            
            for my_object in group_updatable:
                my_object.update(dt)
            for my_object in group_drawable:
                my_object.draw(screen)
            for my_shot in group_shots:
                my_shot.draw(screen)
                
                
            if((my_asteroidfield.active_asteroids)<=1):
                my_asteroidfield.number_of_asteroids=0
                my_asteroidfield.update(dt)

            #check if player hits any asteroids
            for asteroid in group_asteroids:
                my_player.collision(asteroid)
                #check if asteroid hits another asteroid
                group_asteroids_dummy= group_asteroids.copy()
                group_asteroids_dummy.remove(asteroid)
                for asteroid2 in group_asteroids_dummy:
                    asteroid.collision(asteroid2)
                #check if you shot something!
                for my_shot in group_shots:
                    #returns (None, 20) or (hit, 10)
                    asteroid_hit=my_shot.collision(asteroid)
                    my_player.score+=asteroid_hit[1]
                    #print(my_player.score)
                    if(asteroid_hit[0]=="hit"):
                        random_angle=random.uniform(20,50)
                        my_asteroidfield.spawn((asteroid.radius-c.ASTEROID_MIN_RADIUS),asteroid.position,(asteroid.velocity.rotate(-random_angle))*1.2)
                        my_asteroidfield.spawn((asteroid.radius-c.ASTEROID_MIN_RADIUS),asteroid.position,(asteroid.velocity.rotate(+random_angle))*1.2)
                        my_asteroidfield.active_asteroids+=1
                        asteroid.kill()
                    elif(asteroid_hit[0]=="kill"):
                        my_asteroidfield.active_asteroids-=1
                        print(f"{my_asteroidfield.active_asteroids} - {my_asteroidfield.number_of_asteroids} ")
                    
            

            score_text = font.render(f"Score: {my_player.score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
            #Einde van de loop!! 
            pygame.display.flip()

    except SystemExit:
        print("clean exit")
        sys.exit()

    


#deze lijn zorgt ervoor dat de code enkel runt als de filenaam main.py opgeroepen wordt
#python3 main.py
if __name__ == "__main__":
    #print(dir(c))  # This will list all attributes in the module
    main()
