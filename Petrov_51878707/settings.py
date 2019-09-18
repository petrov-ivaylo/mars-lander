import pygame

class Settings():
       """A class to store all top-level game settings for Pong."""
       def __init__(self):
           """Initialize the game's settings."""

           # Screen settings
           self.screen_width = 960
           self.screen_height = 600

           # Background 
           self.bg_colour = pygame.image.load("mars_background.png")
           self.mars_back = self.bg_colour.get_rect()

           # Game settings
           self.lives = 3