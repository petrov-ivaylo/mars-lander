import sys
import pygame
import components
import random

pygame.font.init()

import time
#Pygame start function

pygame.init()
# Create the clock
#clock = pygame.time.Clock()
# A simple loop of 10 stages



def check_events(lander,thrust):
    """Respond to key presses"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and lander.disable1 == False:
                # move lander right
                lander.move_right()
                thrust.move_right()
            elif event.key == pygame.K_LEFT and lander.disable2 == False:
                # move lander left
                lander.move_left()
                thrust.move_left()
            elif event.key == pygame.K_SPACE and lander.disable3 == False:
                # make the thrust visible
                thrust.visible = True


def update_screen(settings, screen, lander, thrust, pad1, pad2, pad3, instruments):
    """Update objects on the screen."""

    # displaying all the instruments on the instrument panel
    screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(pygame.time.get_ticks() / 1000, 2)), False, (255,0,0)), (50,6))
    screen.blit(pygame.font.SysFont('Arial', 12).render(str(components.return_score()), False, (255, 0, 0)),(55, 52))
    screen.blit(pygame.font.SysFont('Arial', 12).render(str(thrust.fuel), False, (255, 0, 0)), (55, 20))
    screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(lander.x_veloc,2)), False, (255, 0, 0)), (190, 20))
    screen.blit(pygame.font.SysFont('Arial', 12).render(str(round(lander.y_veloc,2)), False, (255, 0, 0)), (190, 35))
    screen.blit(pygame.font.SysFont('Arial', 12).render(str(1000 - components.return_altitude()), False, (255, 0, 0)), (190, 6))
    screen.blit(pygame.font.SysFont('Arial', 12).render(str(lander.damage), False, (255, 0, 0)), (60, 35))

    pygame.display.flip()

    screen.blit(settings.bg_colour, settings.mars_back)

    # Refresh the display of the 3 game objects
    #wall.blitme()
    #bat.blitme()
    #ball1.blitme()
    #ball2.blitme()
    #thrust.blitme()
    lander.blitme()



    # display the thrust and update all characteristics connected with it
    if thrust.visible == True and thrust.fuel > 0:

        thrust.blitme()
        thrust.fuel -= 5    # decrease the fuel of the lander by 5 every time we press SPACE
        if lander.x_veloc < 0:
            lander.x_veloc += 0.33
            thrust.x_veloc += 0.33
        elif lander.x_veloc > 0:
            lander.x_veloc -= 0.33
            thrust.x_veloc -= 0.33
        lander.y_veloc -= 0.33
        thrust.y_veloc -= 0.33
        thrust.visible = False

    # displaying the three random pads
    screen.blit(pad1.image, pad1.rect)
    screen.blit(pad2.image, pad2.rect)
    screen.blit(pad3.image, pad3.rect)

    instruments.blitme()
    for i in range(len(components.return_obstacles_list())):    # displaying the obstacles

        screen.blit(components.return_obstacles_list()[i].image, (components.return_obstacles_list()[i].rect.centerx,components.return_obstacles_list()[i].rect.centery))


    # Make the most recently drawn screen visible.
    pygame.display.flip()
