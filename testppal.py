import os,sys,pygame
from pygame.locals import *
from gui.guiclasses import *
from simulator import Simulator
from gui.screen_algorithms import *
from gui.base_gui import *
screen_size = (1000, 640)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
butt_list=[{'action':'esta', 'img':"gui/img/button.png"},{'action':'otra', 'img':"gui/img/button.png"},{'action':'miraqloco', 'img':"gui/img/button.png"},{'action':'otrama', 'img':"gui/img/button.png"}]

pygame.init()
s = pygame.display.set_mode(screen_size)
mrect = (0, 0, s.get_width(), s.get_height()/8)
m = Menu(s, mrect, white, butt_list, True)
irect = (0,s.get_height()/8,s.get_width(),7 * s.get_height()/8)
i = InputBox(s, irect, (100,100,100))
pygame.display.flip()


run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for button in m.elements:
                if button.clicked(pos):
                    print button.action
        if event.type == pygame.QUIT:
            run = False
        #faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
pygame.quit()
sys.exit(), 


