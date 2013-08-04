# import os
import sys
import pygame
from pygame.locals import *
from simulator import Simulator
from gui import *
#---------------
# helpers
# --------------
def init_home_screen(main_screen,screen_size):
    home_rect = (0, 0, screen_size[0], screen_size[1])
    home_screen = Screen(main_screen, home_rect, black)
    home_buttons = [
                    {'id':1, 'obj': home_screen, 'action': 'go_forward', 'img': "gui/img/back.jpg"},
                    {'id':2, 'obj': home_screen, 'action': 'go_back', 'img': "gui/img/back.jpg"}
                   ]
    home_menu = Menu(home_screen, (0, 0, main_screen.get_width(), main_screen.get_height()/6), black, home_buttons, True)
    home_screen.add_elements(home_menu)
    home_screen.update_sfc()
    return home_screen

def init_algorithm_screen(main_screen,screen_size):
    buttons = [
                # {'obj': algoritmos, 'action': 'go_back',  'img': "gui/img/button_small.png"},
                {'id':3, 'obj': sim, 'action': 'executeFCFS', 'img': "gui/img/fcfs.png"},
                {'id':3, 'obj': sim, 'action': 'executeCLOOK', 'img': "gui/img/clook.png"},
                {'id':3, 'obj': sim, 'action': 'executeLOOK',  'img': "gui/img/look.png"},
                {'id':3, 'obj': sim, 'action': 'executeSCAN',  'img': "gui/img/scan.png"},
                {'id':3, 'obj': sim, 'action': 'executeSSTF',  'img': "gui/img/sstf.png"},
                {'id':3, 'obj': sim, 'action': 'executeCSCAN', 'img': "gui/img/cscan.png"},
              ]
    algorithms_screen = Screen(main_screen, (0, 0, screen_size[0], screen_size[1]), black)
    algorithms_menu = Menu(main_screen, (0, 0, main_screen.get_width()/4, main_screen.get_height()), black, buttons, False)
    grect = (algorithms_menu.get_width() + 20, 30, sim.max_tracks + 40, sim.max_tracks + 40)
    algorithms_graphic = Graphic(algorithms_screen, grect, color=(255,255,0))
    algorithms_screen.add_elements(algorithms_menu,algorithms_graphic)
    algorithms_screen.update_sfc()
    algorithms_menu.update_sfc()
    return algorithms_screen
# ----------
# variables
# ----------
screen_size = (1000, 640)
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
# home = Screen(main, home_rect, black)

# home_menu = Menu(home, (0, 0, main.get_width(), main.get_height()/6), black, home_buttons, False)
# initialize algoritmos
print "printeando sim.requirements \n", sim.requirements
# ----------
# pygame loop
# ----------
# screen = Screen(main, home_rect, black)
active_screen = init_algorithm_screen(main, screen_size)
pygame.display.flip()
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            active_menu = active_screen.get_menu()
            print active_menu.elements
            if active_menu.elements:
                for button in active_menu.elements:
                    if button.clicked(pos):
                        print button.id
                        if button.id == 1:
                            algoritmos = Screen(main, (0, 0, screen_size[0], screen_size[1]), black)
                            print "Espere un momento cargando pantalla"
                        elif button.id==3:
                            results = button.executeAction()
                            if results:
                                reqs=results[0][0]
                                active_screen.get_graphic().print_graphic(reqs)
                                active_screen.update_sfc()
                                active_screen.get_menu().update_sfc()
        if event.type == pygame.QUIT:
            run = False
        # faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
pygame.quit()
sys.exit()






            # active_menu = active_screen.get_menu()
            # print active_menu.elements
            # for button in active_menu.elements:
    # for elem in screens:
        # if elem.selected:
            # active_screen = elem 
            # break
                # if button.clicked(pos):
                #     results = button.executeAction()

                    # results = button.executeAction()
                    # print results
                    # if results:
                    #     requirements = results[0][0]
                    #     print "reqs post execute \n", requirements
                        

                    #     g.print_graphic(requirements)
                    #     print 'printing elemenst: \n', algoritmos.elements
                    #     algoritmos.update_sfc()
                    #     m.update_sfc()
