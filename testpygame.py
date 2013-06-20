import sys
#import and init pygame
import pygame


pygame.init() 
#create the screen
window = pygame.display.set_mode((640, 480)) 
lista = [0,50,90,150,160,540]
l = [1, 2, 3, 4, 5, 6]
o = [(l[i],l[i+1]) for i in range(0,len(l),1)]
print lista[0]
#draw a line - see http://www.pygame.org/docs/ref/draw.html for more 
# pygame.draw.lines(window, (255, 255, 255), lista, 1)
pygame.draw.line(window, (255, 255, 255), (0, lista[0]), (0, lista[1]))
pygame.draw.line(window, (255, 255, 255), (0, lista[2]), (0, lista[3]))
# pygame.draw.line(window, (255, 255, 255), (0, 0), (lista[4], lista[5]))
#draw it to the screen
pygame.display.flip() 
#input handling (somewhat boilerplate code):
while True: 
   for event in pygame.event.get(): 
     if event.type == pygame.QUIT: 
       sys.exit(0) 
     else: 
       print event