import os,sys,pygame
from pygame.locals import *
from gui.screen_algorithms import ScreenAlgorithms
from gui.buttons import BaseButton
from simulator import Simulator
# import simulator
#from pimb import pimb
# colores
gray  = (150,150,150)
black = (255,255,255)
#inicio pygame
pygame.init()
screen = pygame.display.set_mode((1024,702))
screen.fill(gray)

# botones
#--------
lote = Simulator()
lote.random_list(15)
lote.add_random_pf(5)
button = BaseButton(lote, "executeLOOK", (10,10), "gui/img/button_small.png")
# button = BaseButton(lote, "executeCLOOK", (100,100), "gui/img/button_small.png")
# screen.blit(button.img, button.rect)
# screen.blit(button2.img, button2.rect)

#creamos superficie grafico
g = ScreenAlgorithms((1024,702),black,lote)
screen.blit(g.graphic_screen,(0,0))
# g.print_leyends('SSTF','345', True)
# g.print_graphic()
# g.print_reqs_attended() 

clock = pygame.time.Clock()
pygame.display.flip()
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        # print event
        if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          # for button in menu.buttons:
          #   if button.img.get_rect().collidepoint(pos):
                  # print button.executeAction()
          # if button.img.get_rect().collidepoint(pos):
            # n = Button()
            # screen.blit(n.img, (200,200))
        results = button.executeAction()
        print results
        reqs = results[0][0]
        movs = str(results[0][1])
        dire = results[0][2]

        g.print_graphic(reqs)
        g.print_leyends(results[1], movs, dire)
            # print button2.executeAction()

            
        screen.blit(g.graphic_screen,(0,0))
        pygame.display.flip()
        if event.type == pygame.QUIT:
            run = False
        #faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
pygame.quit()
sys.exit()    