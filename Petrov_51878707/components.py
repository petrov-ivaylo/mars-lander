import pygame
import random
import settings

global score
score = 0       # at the beginning of the game the player has a score of 0 points

global altitude
altitude = 1000     # at the beginning the lander's altitude is 1000m

# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
pygame.font.init()

import time
#Pygame start function

pygame.init()
# Create the clock
#clock = pygame.time.Clock()
# A simple loop of 10 stages

messagefont = pygame.font.SysFont('Arial', 60)
message = messagefont.render('You Have Crashed!', False, (255, 0, 0))


class Lander:

    x_veloc = random.uniform(-1.0, 1.0)
    y_veloc = random.uniform(0.0, 1.0)

    def __init__(self, screen, settings):
        """Initialize the ball"""
        # Keep a local copy of the screen
        self.screen = screen
        # Load the ball image and get its pygame rect.
        self.image = pygame.image.load('lander.png')
        self.rect = self.image.get_rect()

        # Start each new ball at a random position
        self.rect.centerx = 450
        self.rect.centery = 25

        self.fuel = 500     # the lander has 500kg fuel at the beginning
        self.damage = 0     # the lander has 0% damage at the beginning

        self.disable1 = False   # blocking the left arrow
        self.disable2 = False   # blocking the right arrow
        self.disable3 = False   # blocking the space bar

        self.success = False    # showing whether the lander met a pad with success

    def update(self, meteors_active):

        global altitude
        altitude = int((((self.rect.centery-25)*1.8519)-92))


        # Update the x,y position of the lander
        self.rect.centerx += self.x_veloc
        self.rect.centery += self.y_veloc
        self.y_veloc += 0.1
        if self.x_veloc < 0:
            self.x_veloc -= 0.1
        elif self.x_veloc > 0:
            self.x_veloc += 0.1


        #for i in range(len(obstacles_list)):
         #   if (self.rect.left == obstacles_list[i].rect.right and self.rect.top - obstacles_list[i].rect.top <= 60 and self.rect.top - obstacles_list[i].rect.top >= 0) or (self.rect.right == obstacles_list[i].rect.left and self.rect.top - obstacles_list[i].rect.top <= 60 and self.rect.top - obstacles_list[i].rect.top >= 0) or (self.rect.left == obstacles_list[i].rect.right and self.rect.bottom - obstacles_list[i].rect.top <= 60 and self.rect.bottom - obstacles_list[i].rect.top >= 0) or (self.rect.right == obstacles_list[i].rect.left and self.rect.bottom - obstacles_list[i].rect.top <= 60 and self.rect.bottom - obstacles_list[i].rect.top >= 0):
          #     self.damage += 10

        if self.rect.collidelist(obstacles_list) != -1:     # checking if the lander met an obstacle and increasing its damage by 10%
            self.damage += 10

        if self.rect.collidelist(meteors_list) != -1 and meteors_active == True:    # checking if the lander met a meteor, when they appear, and increasing its damage by 25%
            self.damage += 25



    def move_right(self):
        self.rect.centerx += 20

    def move_left(self):
        self.rect.centerx -= 20

    def blitme(self):
        """Draw the ball at its current location."""
        self.screen.blit(self.image, self.rect)


    def inplay(self, settings, thrust, pad1, pad2, pad3):

        global score
        global altitude
        #if self.rect.bottom >= pad1.rect.top or self.rect.bottom >= pad2.rect.top or self.rect.bottom >= pad3.rect.top:
        if (self.rect.centery - self.y_veloc <= pad1.rect.top - 30 and self.rect.centery >= pad1.rect.top - 30 and pad1.rect.left <= self.rect.left and self.rect.right <= pad1.rect.right and self.x_veloc<= 5 and self.y_veloc <=5 and self.x_veloc >= -5 and self.y_veloc >= -5) or (self.rect.centery - self.y_veloc <= pad2.rect.top - 30 and self.rect.centery >= pad2.rect.top - 30 and pad2.rect.left <= self.rect.left and self.rect.right <= pad2.rect.right and self.x_veloc<= 5 and self.y_veloc <=5 and self.x_veloc >= -5 and self.y_veloc >= -5) or (self.rect.centery - self.y_veloc <= pad3.rect.top - 30 and self.rect.centery >= pad3.rect.top - 30 and pad3.rect.left <= self.rect.left and self.rect.right < pad3.rect.right and self.x_veloc<= 5 and self.y_veloc <=5 and self.x_veloc >= -5 and self.y_veloc >= -5):


            score += 50
            self.success = True

            settings.lives += 1

            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(pygame.time.get_ticks() / 1000, 2)), False,(255, 0, 0)), (50, 6))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(score), False, (255, 0, 0)), (55, 52))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(thrust.fuel), False, (255, 0, 0)), (55, 20))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(self.x_veloc, 2)), False, (255, 0, 0)),(190, 20))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(self.y_veloc, 2)), False, (255, 0, 0)),(190, 35))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(1000 - altitude), False, (255, 0, 0)),  (190, 6))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(self.damage), False, (255, 0, 0)), (60, 35))
            pygame.display.flip()
            return False


        if (self.rect.centery - self.y_veloc <= pad1.rect.top - 30 and self.rect.centery >= pad1.rect.top - 30 and pad1.rect.left <= self.rect.left and self.rect.right <= pad1.rect.right and (self.x_veloc > 5 or self.y_veloc > 5 or self.x_veloc < -5 or self.y_veloc < -5)) or (self.rect.centery - self.y_veloc <= pad2.rect.top - 30 and self.rect.centery >= pad2.rect.top - 30 and pad2.rect.left <= self.rect.left and self.rect.right <= pad2.rect.right and (self.x_veloc > 5 or self.y_veloc > 5 or self.x_veloc < -5 or self.y_veloc < -5)) or (self.rect.centery - self.y_veloc <= pad3.rect.top - 30 and self.rect.centery >= pad3.rect.top - 30 and pad3.rect.left <= self.rect.left and self.rect.right < pad3.rect.right and (self.x_veloc > 5 or self.y_veloc > 5 or self.x_veloc < -5 or self.y_veloc < -5)):
            self.damage = 100
            self.screen.blit(message, (280, 250))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(pygame.time.get_ticks() / 1000, 2)), False,(255, 0, 0)), (50, 6))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(score), False, (255, 0, 0)),(55, 52))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(thrust.fuel), False, (255, 0, 0)), (55, 20))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(self.x_veloc, 2)), False, (255, 0, 0)),(190, 20))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(self.y_veloc, 2)), False, (255, 0, 0)),(190, 35))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(1000 - altitude), False, (255, 0, 0)),(190, 6))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(self.damage), False, (255, 0, 0)), (60, 35))
            pygame.display.flip()
            return False

        #Check if the ball instance is still in play and return T/F
        elif self.rect.centery > settings.screen_height - 35:
            self.damage = 100

            self.screen.blit(message, (280, 250))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(pygame.time.get_ticks() / 1000, 2)), False,(255, 0, 0)), (50, 6))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(score), False, (255, 0, 0)), (55, 52))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(thrust.fuel), False, (255, 0, 0)), (55, 20))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(self.x_veloc, 2)), False, (255, 0, 0)),(190, 20))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(self.y_veloc, 2)), False, (255, 0, 0)),(190, 35))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(1000 - altitude), False, (255, 0, 0)),(190, 6))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(self.damage), False, (255, 0, 0)), (60, 35))
            pygame.display.flip()

            return False

        if self.damage >= 100:
            self.screen.blit(message, (280, 250))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(pygame.time.get_ticks() / 1000, 2)), False,(255, 0, 0)), (50, 6))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(score), False, (255, 0, 0)), (55, 52))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(thrust.fuel), False, (255, 0, 0)), (55, 20))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(self.x_veloc, 2)), False, (255, 0, 0)),(190, 20))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(self.y_veloc, 2)), False, (255, 0, 0)),(190, 35))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(1000 - altitude), False, (255, 0, 0)),(190, 6))
            self.screen.blit(pygame.font.SysFont('Arial', 12).render(str(self.damage), False, (255, 0, 0)), (60, 35))
            pygame.display.flip()

            return False

        return True

    def return_rect(self):
        return self.rect

    def return_rect_centerx(self):
        return self.rect.centerx

    def return_rect_centery(self):
        return self.rect.centery

    def return_x_veloc(self):
        return  self.x_veloc

    def return_y_veloc(self):
        return  self.y_veloc


class Thrust(Lander):

    def __init__(self, screen, settings):

        super().__init__(screen, settings)
        """Initialize the ball"""

        # Keep a local copy of the screen
        self.screen = screen
        # Load the ball image and get its pygame rect.
        self.image = pygame.image.load('thrust.png')
        #self.rect = self.image.get_rect()
        self.rect = super().return_rect()

        # Start each new ball at a random position
        self.rect.centerx += 31.5
        self.rect.centery += 50

        self.visible = False    # make the thrust visible when the space bar is pressed (self.visible = True)

    def blitme(self):

        self.screen.blit(self.image, self.rect)


class Pad:
    choice = random.randint(1,2)    # which kind of pads to load

    def __init__(self, screen, settings):
        """Initialize the ball"""
        # Keep a local copy of the screen
        self.screen = screen
        # Load the ball image and get its pygame rect.
        if self.choice == 1:
            self.image = pygame.image.load('landingPads\pad.png')
        elif self.choice == 2:
            self.image = pygame.image.load('landingPads\pad_tall.png')
        self.rect = self.image.get_rect()

        # Start each new ball at a random position
        self.rect.centerx = 0
        if self.choice == 1:
            self.rect.centery = random.randint(50,settings.screen_height - 18)
        elif self.choice == 2:
            self.rect.centery = random.randint(50,settings.screen_height - 82)

        # Start each new ball with an x & y velocity of 10


class Instruments:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('instruments.png')
        self.rect = self.image.get_rect()
        #print(self.rect.right, self.rect.bottom)

    def blitme(self):
        self.screen.blit(self.image, (0,0))


class Obstacle:

    def __init__(self):

        self.img = random.randint(1,10)     # decide which obstacle to load
        if self.img == 1:
            self.image = pygame.image.load('obstacles\puilding_dome.png')
        elif self.img == 2:
            self.image = pygame.image.load('obstacles\puilding_station_NE.png')
        elif self.img == 3:
            self.image = pygame.image.load('obstacles\puilding_station_SW.png')
        elif self.img == 4:
            self.image = pygame.image.load('obstacles\pipe_ramp_NE.png')
        elif self.img == 5:
            self.image = pygame.image.load('obstacles\pipe_stand_SE.png')
        elif self.img == 6:
            self.image = pygame.image.load('obstacles\wocks_NW.png')
        elif self.img == 7:
            self.image = pygame.image.load('obstacles\wocks_ore_SW.png')
        elif self.img == 8:
            self.image = pygame.image.load('obstacles\wocks_small_SE.png')
        elif self.img == 9:
            self.image = pygame.image.load('obstacles\satellite_SE.png')
        elif self.img == 10:
            self.image = pygame.image.load('obstacles\satellite_SW.png')

        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(230,900)
        self.rect.centery = random.randint(0,550)


class Meteor:

    def __init__(self):

        self.img = random.randint(1,4)      # chose which kind of meteor to load
        if self.img == 1:
            self.image = pygame.image.load('meteors\spaceMeteors_001.png')
        elif self.img == 2:
            self.image = pygame.image.load('meteors\spaceMeteors_002.png')
        elif self.img == 3:
            self.image = pygame.image.load('meteors\spaceMeteors_003.png')
        elif self.img == 4:
            self.image = pygame.image.load('meteors\spaceMeteors_004.png')

        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0,900)
        self.rect.centery = -100


num_obstacles = random.randint(5,10)    # build between 5 and 10 obstacles (at least 5)
global obstacles_list   # a list to store all obstacles
obstacles_list = []

while num_obstacles > 0:
    obstacle = Obstacle()
    obstacles_list.append(obstacle)
    num_obstacles -= 1


num_meteors = random.randint(5,10)      # build between 5 and 10 meteors
global meteors_list
meteors_list = []
while num_meteors > 0:
    meteor = Meteor()
    meteors_list.append(meteor)
    num_meteors -= 1


def return_obstacles_list():
    global obstacles_list
    return obstacles_list

def return_meteors_list():
    global meteors_list
    return meteors_list

def decrease_score():
    global score
    score -= 50

def decrease_lives(settings):
    settings.lives -= 1

def decrease_damage(lander):
    lander.damage -= 10

def return_score():
    global score
    return score

def return_altitude():
    global altitude
    return altitude