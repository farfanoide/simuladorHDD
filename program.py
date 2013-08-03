# import os
import sys
import pygame
from pygame.locals import *
from simulator import Simulator
from gui import *
# ----------
# variables
# ----------
screen_size = (1000, 640)
red         = (255, 0, 0)
green       = (0, 255, 0)
blue        = (0, 0, 255)
white       = (255, 255, 255)
black       = (31, 34, 39)
clock       = pygame.time.Clock()
sim         = Simulator()
sim.random_list(15)
sim.add_random_pf(5)
# b_home =    [
#                 {'obj': s_home, 'action': 'switchSelect', 'img': "gui/img/back.jpg"},
#                 {'obj': s_home, 'action': 'switchSelect', 'img': "gui/img/back.jpg"}
#             ]

# ----------
# main 
# ----------

pygame.init()
s = pygame.display.set_mode(screen_size)


# screen_alg = Screen()
s.fill(black)
mrect = (0, 0, s.get_width(), s.get_height()/8)
irect = (0, s.get_height()/8, s.get_width()/4, s.get_height()/6)
i = InputBox(s, irect, black)
buttons = [
            {'obj': i,   'action': 'ask',          'img': "gui/img/button_small.png"},
            {'obj': sim, 'action': 'executeCLOOK', 'img': "gui/img/CLOOK.jpg"},
            {'obj': sim, 'action': 'executeLOOK',  'img': "gui/img/LOOK.jpg"},
            {'obj': sim, 'action': 'executeSCAN',  'img': "gui/img/SCAN.jpg"},
            {'obj': sim, 'action': 'executeCSCAN', 'img': "gui/img/CSCAN.jpg"},
            {'obj': sim, 'action': 'executeSSTF',  'img': "gui/img/SSTF.jpg"}
          ]
m = Menu(s, mrect, black, buttons, True)
print i.get_width()
grect = (i.get_width() + 20, s.get_height()/8, sim.max_tracks + 40, sim.max_tracks + 40)
# g = Graphic(s, grect, sim.requirements)
# sim.requirements = i.ask()
print "printing padding: ", i.padding
print "printeando sim.requirements \n", sim.requirements

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
                    results = button.executeAction()
                    print results
                    if results:
                        requirements = results[0][0]
                        print "reqs post execute \n", requirements
                        g = Graphic(s, grect, requirements)

        if event.type == pygame.QUIT:
            run = False
        # faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
pygame.quit()
sys.exit()
