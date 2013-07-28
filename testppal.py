import os
import sys
import pygame
from pygame.locals import *
from gui.guiclasses import *
from simulator import Simulator
from gui.screen_algorithms import *
from gui.base_gui import *

# ----------
# variables
# ----------
screen_size = (1000, 640)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()
sim = Simulator()
sim.random_list(15)
sim.add_random_pf(5)
buttons = [
            {'simulator': sim, 'action': 'executeFCFS', 'img': "gui/img/FCFS.jpg"},
            {'simulator': sim, 'action': 'executeCLOOK', 'img': "gui/img/CLOOK.jpg"},
            {'simulator': sim, 'action': 'executeCSCAN', 'img': "gui/img/CSCAN.jpg"},
            {'simulator': sim, 'action': 'executeSSTF', 'img': "gui/img/SSTF.jpg"}
          ]

# ----------
# main 
# ----------

pygame.init()
s = pygame.display.set_mode(screen_size)
mrect = (0, 0, s.get_width(), s.get_height()/8)
m = Menu(s, mrect, white, buttons, True)
irect = (0,s.get_height()/8,s.get_width(),7 * s.get_height()/8)
i = InputBox(s, irect, (100,100,100))
pygame.display.flip()

# ----------
# pygame loop
# ----------
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for button in m.elements:
                if button.clicked(pos):
                    print button.executeAction()
        if event.type == pygame.QUIT:
            run = False
        # faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
pygame.quit()
sys.exit()
