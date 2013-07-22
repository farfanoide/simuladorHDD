import os
import sys
import pygame
from pygame.locals import *
from graphic import Graphic

class SetUpScreen():

	def __init__(self, screen):
		self.screen = screen
		self.screen.fill((255,0,0))


class AlgorithmScreen():

	def __init__(self, screen):
		self.screen = screen
		self.screen.fill((0,0,255))

