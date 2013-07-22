import os,sys,pygame
from pygame.locals import *
from gui.guiclasses import *
from simulator import Simulator
from gui.screen_algorithms import *
# from gui.screen_algorithms import ScreenAlgorithms
##begin
pygame.init()

screen = pygame.display.set_mode((1024,702))
sim = Simulator()
sim.random_list()
sim.add_random_pf(4)
sus = SetUpScreen(screen, (100,100,100), sim)
als = AlgorithmScreen(screen, (100,100,100), sim)
run = True

while run:
    if sus.selected:
        buttons = sus.buttons
        sus.showScreen()
    else:
        buttons = als.buttons
        als.showScreen()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                print button.id
                if button.clicked(pos):
                    print button.id
                    if button.id < 100:
                        results = button.executeAction()
                        print results
                        reqs = results[0][0]
                        movs = str(results[0][1])
                        dire = results[0][2]
                        als.print_graphic(reqs)
                        als.print_leyends(results[1],results[0][1],results[0][2])
                        screen.blit(als.graphic_screen,(200,0))
                        pygame.display.update()
                    else:
                        sus.switchSelect()

        if event.type == pygame.QUIT:
            run = False
        #faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
pygame.quit()
sys.exit()    


