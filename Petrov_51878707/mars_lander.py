import pygame
import random

from settings import Settings
from components import Lander
from components import Thrust
from components import Pad
from components import Instruments
import components
import game_functions as gf

import time
#Pygame start function

def run_game():
    """Main function to start game and run top-level loop"""
    # Initialize pygame, settings and screen object.
    pygame.init()
    # Set keys to repeat if held down.
    pygame.key.set_repeat(25,25)
    # Create settings object containing game settings
    settings = Settings()
    # Create the main game screen
    screen = pygame.display.set_mode( (settings.screen_width, settings.screen_height))
    # Fill the game screen with BLACK colour
    screen.blit(settings.bg_colour,settings.mars_back)
    # Create a main window caption
    pygame.display.set_caption("Mars Lander - Ivaylo Petrov - 51878707")

    # create all pads and set their coordinates to satisfy our expectations
    pad1 = Pad(screen, settings)

    pad1.rect.centerx = random.randint(75, 265)
    pad1.rect.centery = random.randint(100,600)

    pad2 = Pad(screen, settings)

    pad2.rect.centerx = random.randint(425, 535)

    pad3 = Pad(screen, settings)

    pad3.rect.centerx = random.randint(695, 885)

    while settings.lives > 0:
        global meteors_active
        meteors_active = False

        # Make the wall
        lander = Lander(screen,settings)
        thrust = Thrust(screen,settings)
        instruments = Instruments(screen)



         # Start the main loop for the game.
        while lander.inplay(settings, thrust, pad1, pad2, pad3):

            if lander.rect.centerx >= 960:
                lander.rect.centerx = 40
                thrust.rect.centerx = 71.5
            if lander.rect.centerx <= 0:
                lander.rect.centerx = 960
                thrust.rect.centerx = 991.5

            if lander.rect.centery <= 25:
                lander.rect.centery = 25
                thrust.rect.centery = 75

            # Watch for keyboard events.
            gf.check_events(lander, thrust)

            # Update the lander (if still in play)
            if lander.inplay(settings, thrust, pad1, pad2, pad3):

                lander.update(meteors_active)
                thrust.update(meteors_active)

                which_key = random.randint(1, 3)

                if random.randint(1, 50) == 1:      # 1:50 chance to have a not working key

                    current_time = pygame.time.get_ticks()
                    while pygame.time.get_ticks() - current_time <= 2000:   # block a key for 2 seconds

                        if lander.rect.centerx >= 960:
                            lander.rect.centerx = 40
                            thrust.rect.centerx = 71.5
                        if lander.rect.centerx <= 0:
                            lander.rect.centerx = 960
                            thrust.rect.centerx = 991.5

                        if lander.rect.centery <= 25:
                            lander.rect.centery = 25
                            thrust.rect.centery = 75

                        screen.blit(pygame.font.SysFont('Arial', 16).render("Alert", False, (0, 0, 255)),(150, 52))     # showing the "Alert" message
                        pygame.display.flip()

                        gf.check_events(lander, thrust)
                        lander.update(meteors_active)
                        thrust.update(meteors_active)
                        gf.update_screen(settings, screen, lander, thrust, pad1, pad2, pad3, instruments)

                        if not lander.inplay(settings, thrust, pad1, pad2, pad3) and lander.success == True:
                            # decrease the score and lives, because by checking if the lander is still in play we increase them one more time
                            components.decrease_score()
                            components.decrease_lives(settings)
                            #components.decrease_damage(lander)
                            lander.success = False
                            break
                        elif not lander.inplay(settings, thrust, pad1, pad2, pad3) and lander.success == False:
                            break

                        # choose which key to be blocked
                        if which_key == 1:
                            lander.disable1 = True
                        elif which_key == 2:
                            lander.disable2 = True
                        elif which_key == 3:
                            lander.disable3 = True



                    lander.disable1 = False
                    lander.disable2 = False
                    lander.disable3 = False

                if random.randint(1, 75) == 1:      # 1:75 chance to have falling meteors
                    meteors_active = True
                    change_x = random.uniform(-5,5)
                    for i in range(len(components.return_meteors_list())):
                        while components.return_meteors_list()[i].rect.centery <= 600:
#                            components.return_meteors_list()[i].rect.centery += 5

                            if lander.rect.centerx >= 960:
                                lander.rect.centerx = 40
                                thrust.rect.centerx = 71.5
                            if lander.rect.centerx <= 0:
                                lander.rect.centerx = 960
                                thrust.rect.centerx = 991.5

                            if lander.rect.centery <= 25:
                                lander.rect.centery = 25
                                thrust.rect.centery = 75


                            for j in range(len(components.return_meteors_list())):
                                components.return_meteors_list()[j].rect.centery += 5
                                components.return_meteors_list()[j].rect.centerx += change_x

                                screen.blit(components.return_meteors_list()[j].image, (components.return_meteors_list()[j].rect.centerx, components.return_meteors_list()[j].rect.centery))
                                pygame.display.flip()

                            if not lander.inplay(settings, thrust, pad1, pad2, pad3) and lander.success == True:
                                components.decrease_score()
                                components.decrease_lives(settings)
                                # components.decrease_damage(lander)
                                lander.success = False
                                meteors_active = False
                                for j in range(len(components.return_meteors_list())):
                                    components.return_meteors_list()[j].rect.centery = -100
                                    components.return_meteors_list()[j].rect.centerx = random.randint(0,900)
                                break
                            elif not lander.inplay(settings, thrust, pad1, pad2, pad3) and lander.success == False:
                                meteors_active = False
                                for j in range(len(components.return_meteors_list())):
                                    components.return_meteors_list()[j].rect.centery = -100
                                    components.return_meteors_list()[j].rect.centerx = random.randint(0,900)
                                break

                            gf.check_events(lander, thrust)
                            lander.update(meteors_active)
                            thrust.update(meteors_active)
                            gf.update_screen(settings, screen, lander, thrust, pad1, pad2, pad3, instruments)

                        meteors_active = False



                #for i in range(len(components.return_meteors_list())):
                 #   components.return_meteors_list()[i].rect.centery = 0
                  #    components.return_meteors_list()[i].rect.centerx = random.randint(0,900)


            
            # Now update the sprites, etc. on the screen
            gf.update_screen(settings, screen, lander, thrust, pad1, pad2, pad3, instruments)

        # Wait for a key or mouse event to continue
        null_event = pygame.event.wait() 
        settings.lives -= 1

    # GAME ENDS 

# Call the main method to start the game        
run_game()
