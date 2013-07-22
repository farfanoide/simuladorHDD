import os
import sys
import pygame
from pygame.locals import *
from buttons import BaseButton

class OpenningScreen():

	def __init__(self, screen,background_colour):
		self.screen = screen
		self.bkg_colour = background_colour
		self.screen.fill(self.bkg_colour)




