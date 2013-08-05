# import os
import sys
import pygame
from pygame.locals import *
from simulator import Simulator
from gui import *
# ----------
# variables
# ----------
screen_size = (1000, 740)
black = (31, 34, 39)
clock       = pygame.time.Clock()
sim         = Simulator()

sim.random_list(15)
sim.add_random_pf(5)

# ----------
# main 
# ----------


pygame.init()
main = pygame.display.set_mode(screen_size)
main.fill(black)

# initialize home
home_rect = (0, 0, screen_size[0], screen_size[1])
home = Screen(main, home_rect, black)

home_buttons = [
                {'obj': home, 'action': 'go_back', 'img': "gui/img/back.jpg"},
                {'obj': home, 'action': 'go_back', 'img': "gui/img/back.jpg"}
               ]
home_menu = Menu(home, (0, 0, main.get_width(), main.get_height()/6), black, home_buttons, False)
# initialize algoritmos
algoritmos = Screen(main, (0, 0, screen_size[0], screen_size[1]), black)
buttons = [
            {'obj': algoritmos, 'action': 'go_back',  'img': "gui/img/button_small.png"},
            {'obj': sim, 'action': 'executeFCFS', 'img': "gui/img/fcfs.png"},
            {'obj': sim, 'action': 'executeCLOOK', 'img': "gui/img/clook.png"},
            {'obj': sim, 'action': 'executeLOOK',  'img': "gui/img/look.png"},
            {'obj': sim, 'action': 'executeSCAN',  'img': "gui/img/scan.png"},
            {'obj': sim, 'action': 'executeCSCAN', 'img': "gui/img/cscan.png"},
            {'obj': sim, 'action': 'executeSSTF',  'img': "gui/img/sstf.png"}
          ]
m = Menu(main, (0, 0, main.get_width()/4, main.get_height()), black, buttons, False)
grect = (m.get_width() + 20, 30, sim.max_tracks + 40, sim.max_tracks + 40)
g = Graphic(algoritmos, grect, color=(255,255,0))

# initialize help
# help = Screen(main, (0, 0, screen_size[0], screen_size[1]), black)

footer_buttons =    [
                        {'obj': '', 'action': '', 'img': 'gui/img/method.png'},
                        {'obj': '', 'action': '', 'img': 'gui/img/movs.png'},
                        {'obj': '', 'action': '', 'img': 'gui/img/dir.png'}
                    ]
# footer = Menu

algoritmos.add_elements(m,g)

def serialize_data(results):
    y_offset = 15
    requirements = results[0][0]
    movements = results[0][1]
    direction = "Izquierda" if results[0][2] else "Derecha"
    method = results[1]

    data = [(method,(108,y_offset)), (movements, (160,y_offset-2)), (direction, (130,y_offset))]
    return requirements, data

# irect = (0, s.get_height()/8, s.get_width()/4, s.get_height()/6)
# i = InputBox(s, irect, black)
# g = Graphic(s, grect, sim.requirements)
# sim.requirements = i.ask()
# print "printing padding: ", i.padding
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
                        reqs, data = serialize_data(results)
                        f = Menu(main, (m.get_width()-20, main.get_height()-80, main.get_width()-m.get_width()+20, main.get_height()-g.get_height()+20), black, footer_buttons, True)
                        f.update_captions(data)
                        print "reqs post exe,cute \n", reqs
                        g.print_graphic(reqs)
                        print 'printing elemenst: \n', algoritmos.elements
                        algoritmos.update_sfc()
                        m.update_sfc()
                        f.update_sfc()

        if event.type == pygame.QUIT:
            run = False
        # faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
pygame.quit()
sys.exit()
