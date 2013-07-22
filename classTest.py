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
button = BaseButton(lote, (10,10), "executeLOOK", "gui/img/LOOK.jpg")
button2 = BaseButton(lote, (10,70), "executeCLOOK","gui/img/CLOOK.jpg")
button3 = BaseButton(lote, (10,130), "executeCSCAN","gui/img/CSCAN.jpg")
button4 = BaseButton(lote, (10,190), "executeSCAN","gui/img/SCAN.jpg")
button5 = BaseButton(lote, (10,250), "executeFCFS","gui/img/FCFS.jpg")
button6 = BaseButton(lote, (10,310), "executeSSTF","gui/img/SSTF.jpg")

buttons = []
buttons.append(button)
buttons.append(button2)
buttons.append(button3)
buttons.append(button4)
buttons.append(button5)
buttons.append(button6)
# screen.blit(button2.img, button2.rect)

#creamos superficie grafico
g = ScreenAlgorithms((1024,702),black,lote)
screen.blit(button.img, button.pos)
screen.blit(button2.img, button2.pos)
screen.blit(button3.img, button3.pos)
screen.blit(button4.img, button4.pos)
screen.blit(button5.img, button5.pos)
screen.blit(button6.img, button6.pos)
# g.print_leyends('SSTF','345', True)
# g.print_reqs_attended() 
# cursor = BaseButton(lote,(10,10))

# clock = pygame.time.Clock()
pygame.display.flip()
run = True
while run:
    # g.print_canvas()
    # g.graphic_screen.blit(g.graphic.canvas_sfc, (0,0))    
    #clock.tick(30)
    for event in pygame.event.get():
        # print event


        if event.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()
          for button in buttons:
              if button.clicked(pos):
                # g.print_canvas()
                #g.graphic.graphic_sfc.blit(g.graphic.canvas_sfc,(0,0))
                results = button.executeAction()
                print results
                reqs = results[0][0]
                movs = str(results[0][1])
                dire = results[0][2]
                g.print_graphic(reqs)
                g.print_leyends(results[1],results[0][1],results[0][2])
                screen.blit(g.graphic_screen,(200,0))
                # g.graphic_screen.blit(g.graphic.canvas_sfc,(0,0))
                #pygame.display.flip() 
                # g.graphic_screen.blit(g.graphic.canvas_sfc, (0,0))  
                pygame.display.update() 
          # for button in 

          # for button in menu.buttons:
          #   if button.img.get_rect().collidepoint(pos):
                  # print button.executeAction()
          # if button.img.get_rect().collidepoint(pos):
            # n = Button()
            # screen.blit(n.img, (200,200))
        # results = button.executeAction()

        # g.print_graphic(reqs)
        # g.print_leyends(results[1], movs, dire)
            # print button2.executeAction()


        if event.type == pygame.QUIT:
            run = False
        #faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
pygame.quit()
sys.exit()    