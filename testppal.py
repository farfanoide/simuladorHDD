import os,sys,pygame
from pygame.locals import *
from gui.guiclasses import *
from simulator import Simulator
from gui.screen_algorithms import *
# pygame.Surface
# var
screen_size = (1000, 640)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
butt_list=[{'action':'sometext', 'img':"img/button.png"},{'action':'sometext', 'img':"img/button.png"},{'action':'sometext', 'img':"img/button.png"},{'action':'sometext', 'img':"img/button.png"}]

pygame.init()
s = pygame.display.set_mode(screen_size)
mrect = (0, 0, s.get_width()/3, s.get_height())
m = Menu(s, mrect, white, butt_list, False)
# m = Main(screen_size)
# m.initiate_elements()
# m.menu.populate_sfc(butt_list)
pygame.display.flip()
for button in m.buttons:
    print button.start_y
    print button.start_x
# print screen.get_width()




run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        # print event
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for button in m.menu.buttons:
                if button.clicked(pos):
                    print button.img.get_clip()
            #         print button.img.get_abs_parent().get_rect()
                    # print super(Button, button).get_rect()
            
            # screen.blit(n.img, (200,200))
            # pygame.display.flip()
        if event.type == pygame.QUIT:
            run = False
        #faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
# pygame.quit()
# sys.exit(), 


