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
    """initializes the Home screen (Set up)"""
    home_rect = (0, 0, sz[0], sz[1])
    home_screen = Screen(ms, home_rect, black)
    home_input_box = InputBox(home_screen,(home_screen.get_width()/2-300,home_screen.get_height()/2-100,600,200))
    home_buttons = [
                    {'id':1, 'obj': home_input_box, 'action': 'ask', 'img': "gui/img/input_random.png"},
                    {'id':3, 'obj': home_input_box, 'action': '', 'img': "gui/img/input_arch.png"},
                    {'id':2, 'obj': home_input_box, 'action': 'ask', 'img': "gui/img/input_hand.png"},
                    {'id':4, 'obj': home_input_box, 'action': 'ask', 'img': "gui/img/init.png"}
                   ]
    exec_button = Button(home_screen, 5, '', '', 'gui/img/exec.png')
    exec_button.rect.x = 370
    exec_button.rect.y = 500
    exec_button.update_sfc()
    home_menu = Menu(home_screen, (0, 0, home_screen.get_width(), home_screen.get_height()/6), black, home_buttons, True)
    home_menu.add_elements(exec_button)
    home_screen.add_elements(home_menu,home_input_box)
    return home_screen, home_menu

def init_algorithm_screen(ms,sz,s):
    """initializes Graphic screen"""
    algorithm_buttons = [
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
    return algorithms_screen,algorithms_menu

def serialize_data(results):
    """ Format data to show as result of a certain algorithm"""
    y_offset = 15
    requirements = results[0][0]
    movements = results[0][1]
    method = results[1]
    direction = "Derecha" if results[0][2] else "Izquierda"
    data = [(method,(108,y_offset)), (movements, (160,y_offset-2)), (direction, (130,y_offset))]
    return requirements, data

def load_file(name):
    """ Load data from a file"""
    try:
        f = open(name,'r')
        lines = f.readlines()
        final = ""
        for line in lines:
            final += line
        num_list = final.rsplit(' ')
        full_list = [int(elem) for elem in num_list]
        return full_list
    except IOError:
        return None



def print_message(message, rect, base_sfc, color=(255,255,255)):
    """Prints a message on screen"""
    pygame.font.init()
    font = pygame.font.SysFont(None,20)
    y = rect[1]
    for line in message:
        m = font.render(line, True, color)
        base_sfc.blit(m,(rect[0], y + m.get_height(),rect[2], rect[3]))
        y += m.get_height()
        base_sfc.update_sfc()

#----------------
# DATA
#----------------
footer_buttons =    [
    {'id': -7, 'obj': '', 'action': '', 'img': 'gui/img/method.png'},
    {'id': -7, 'obj': '', 'action': '', 'img': 'gui/img/movs.png'},
    {'id': -7, 'obj': '', 'action': '', 'img': 'gui/img/dir.png'}
]

message_input_random=["Ingrese cantidad deseada de requerimientos y  page faults separados por un espacio."," Ej:20 5 . Para finalizar ingreso presione enter"]
message_input_hand=["Ingrese los requerimientos separados por un espacio(anteponga page faults con '-'."," Ej:20 5 -34"]
message_input_file=["Ingrese nombre del archivo(ejemplo.extension). Debe estar en la carpeta principal del programa"," y con igual formato que el ingreso manual"]
message_input_pos=["Ingrese la posicion inicial. Debe estar entre 0 y 511"]

# ----------
# variables
# ----------
screen_size = (1000, 700)
black = (31, 34, 39)
clock = pygame.time.Clock()
sim   = Simulator()



# ----------
# main
# ----------


pygame.init()
main = pygame.display.set_mode(screen_size)
main.fill(black)
pygame.display.set_caption("HDD Pymulator")
# home men is the menu obj of the screen. Same with algorithm_men
home,home_men = init_home_screen(main, screen_size)
algorithm, algorithm_men = init_algorithm_screen(main, screen_size,sim)
active_screen = home

run = True
active_screen.update_sfc()
while run:
    clock.tick(30)
    error_msg_rect = (200,200,active_screen.get_width(),active_screen.get_height())
    help_msg_rect = (200,active_screen.get_height()/6,active_screen.get_width(), active_screen.get_width())
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if active_screen == home:
                for button in home_men.elements:
                    if button.clicked(pos):
                        if  button.id == 1:
                            print_message(message_input_random,help_msg_rect,home)
                            param_lst = button.executeAction()
                            if param_lst[0]<0 or param_lst[1]<0:
                                print_message(["parametros incorrectos"], error_msg_rect, active_screen,(255,0,0))
                                break
                            sim.random_list(param_lst[0])
                            sim.add_random_pf(param_lst[1]+2)
                        elif button.id == 2:
                            print_message(message_input_hand,help_msg_rect,home)
                            sim.requirements = button.executeAction()
                        elif button.id == 3:
                            print_message(message_input_file,help_msg_rect,home)
                            file_name = active_screen.get_element('InputBox').ask(False)
                            sim.requirements = load_file(file_name)
                            if (sim.requirements == None):
                                print_message(["No se pudo abrir el archivo. Revise permisos y/o ubicacion"],error_msg_rect,active_screen,(255,0,0))
                                break
                        elif button.id == 4:
                            print_message(message_input_pos,help_msg_rect,active_screen)
                            num = active_screen.get_element('InputBox').ask(False)
                            sim.init_pos = int(num)
                            if sim.init_pos<0 or sim.init_pos>511:
                                print_message(["parametros incorrectos"], error_msg_rect,active_screen,(255,0,0))
                                break
                        elif button.id == 5:
                            active_screen=algorithm
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
        if event.type == pygame.QUIT:
            run = False
        # faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
pygame.quit()
sys.exit()
