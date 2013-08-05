# import os
import sys
import pygame
from pygame.locals import *
from simulator import Simulator
from gui import *
#---------------
# helpers
# --------------
def init_home_screen(ms,sz):
    home_rect = (0, 0, sz[0], sz[1])
    home_screen = Screen(ms, home_rect, black)
    home_input_box = InputBox(home_screen,(home_screen.get_width()/4,home_screen.get_height()/2,home_screen.get_width()/2,2*home_screen.get_height()/6))
    home_buttons = [
                    {'id':1, 'obj': home_screen, 'action': '', 'img': "gui/img/back.jpg"},
                    {'id':1, 'obj': home_screen, 'action': '', 'img': "gui/img/back.jpg"},
                    {'id':2, 'obj': home_input_box, 'action': 'ask', 'img': "gui/img/back.jpg"}
                   ]
    home_menu = Menu(home_screen, (0, 0, home_screen.get_width(), home_screen.get_height()/6), black, home_buttons, True)
    home_screen.add_elements(home_menu,home_input_box)
    return home_screen, home_menu

def init_algorithm_screen(ms,sz,s):
    algorithm_buttons = [
                # {'obj': algoritmos, 'action': 'go_back',  'img': "gui/img/button_small.png"},
                {'id':-1, 'obj': s, 'action': 'executeFCFS', 'img': "gui/img/fcfs.png"},
                {'id':-1, 'obj': s, 'action': 'executeCLOOK', 'img': "gui/img/clook.png"},
                {'id':-1, 'obj': s, 'action': 'executeLOOK',  'img': "gui/img/look.png"},
                {'id':-1, 'obj': s, 'action': 'executeSCAN',  'img': "gui/img/scan.png"},
                {'id':-1, 'obj': s, 'action': 'executeSSTF',  'img': "gui/img/sstf.png"},
                {'id':-1, 'obj': s, 'action': 'executeCSCAN', 'img': "gui/img/cscan.png"}
              ]
    algorithms_screen = Screen(ms, (0, 0, sz[0], sz[1]), black)
    algorithms_menu = Menu(algorithms_screen, (0, 0, algorithms_screen.get_width()/4, algorithms_screen.get_height()), black, algorithm_buttons, False)
    grect = (algorithms_menu.get_width() + 20, 30, s.max_tracks + 40, s.max_tracks + 40)
    algorithms_graphic = Graphic(algorithms_screen, grect, black)
    algorithms_screen.add_elements(algorithms_menu,algorithms_graphic)
    # algorithms_screen.update_sfc()
    return algorithms_screen,algorithms_menu

def serialize_data(results):
    y_offset = 15
    requirements = results[0][0]
    movements = results[0][1]
    method = results[1]
    direction = "Izquierda" if results[0][2] else "Derecha"
    data = [(method,(108,y_offset)), (movements, (160,y_offset-2)), (direction, (130,y_offset))]
    return requirements, data

footer_buttons =    [
    {'id': -7, 'obj': '', 'action': '', 'img': 'gui/img/method.png'},
    {'id': -7, 'obj': '', 'action': '', 'img': 'gui/img/movs.png'},
    {'id': -7, 'obj': '', 'action': '', 'img': 'gui/img/dir.png'}
]


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

# home = Screen(main, home_rect, black)

# home_menu = Menu(home, (0, 0, main.get_width(), main.get_height()/6), black, home_buttons, False)
# initialize algoritmos
# print "printeando sim.requirements \n", sim.requirements
# ----------
# pygame loop
# ----------
# screen = Screen(main, home_rect, black)
# print type(algorithms)
# print "home" ,home.get_element("Menu").elements
# print_shite(home.elements)
# print "algorithms" ,algorithms.get_element("Menu").elements
# print_shite(algorithms.elements)
# screens[i].update_sfc()

# print type(active_screen)
# pygame.display.flip()
home,home_men = init_home_screen(main, screen_size)
print home_men.elements


run = True
algorithm, algorithm_men = init_algorithm_screen(main, screen_size,sim)
print algorithm_men.elements
active_screen = home
active_screen.update_sfc()
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if active_screen == home:
                for button in home_men.elements:
                    if button.clicked(pos):
                        if  button.id == 1:
                            active_screen = algorithm
                            active_screen.update_sfc()
                        elif button.id == 2:
                            sim.requirements = button.get_element('InputBox').ask(False)
                            active_screen.update_sfc()
            elif active_screen == algorithm:
                for button in algorithm_men.elements:
                    if button.clicked(pos):
                        if button.id == -1:
                            results = button.executeAction()
                            print "aqui esta wally"
                            if results:
                                reqs, data = serialize_data(results)
                                f = Menu(main, (algorithm_men.get_width()-20, main.get_height()-80, main.get_width()-algorithm_men.get_width()+20, main.get_height()-algorithm.get_element("Graphic").get_height()+20), black, footer_buttons, True)
                                f.update_captions(data)
                                algorithm.get_element("Graphic").print_graphic(reqs)
                                algorithm.update_sfc()
                                algorithm_men.update_sfc()
                                f.update_sfc()
                                # requirements = results[0][0]

                                # print reqs
                                # active_screen.fill(black)

                                # screens[i].get_element("Graphic").print_graphic(reqs)
                                # active_screen.get_element("Graphic").update_sfc()
                                # graph.update_sfc()
                                # active_screen.get_element("Menu").update_sfc()
                                # screens[i].update_sfc()
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
