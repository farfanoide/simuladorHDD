import sys
#import and init pygame
import pygame


pygame.init() 


WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)


#create the screen

window = pygame.display.set_mode((640, 480)) 

pygame.display.set_caption("tuviejaaaaa!!!")

window.fill(WHITE)
l = [0,50,90,150,160,540]
# l = [1, 2, 3, 4, 5, 6]
# o = [((l[i]), y),((l[i+1],y) for i in range(0,len(l),2)]
o = []
y = 10
for i in range(0,len(l)):
    # tup = ((l[i], y), (l[i+1],y+10))
    y += 10
    o.append((l[i], y))
print o
for elem in o:
    print type(elem)
    print elem
    # pygame.draw.aaline(window, (255, 0, 0), elem[0], elem[1], 0)    
pygame.draw.aalines(window, RED, True, o)
# print lista[0]
for x in range(0,640,20):
    pygame.draw.aaline(window, BLACK, (x, 0), (x, 480))
for y in range(0,480,20):
    pygame.draw.aaline(window, GREEN, (0, y), (640, y))
# i=0
# for j in range(0,len(l)):
#     c1=(i,l[j])
    
#draw a line - see http://www.pygame.org/docs/ref/draw.html for more 
# pygame.draw.lines(window, (255, 255, 255), lista, 1)
# pygame.draw.line(window, (255, 255, 255), (0, lista[0]), (0, lista[1]))
# pygame.draw.lines(window, (255, 255, 255), (0, lista[2]), (0, lista[3]))
# pygame.draw.line(window, (255, 0, 0), (0, 0), (lista[4], lista[5]))
#draw it to the screen
pygame.display.flip() 
#input handling (somewhat boilerplate code):
while True: 
   for event in pygame.event.get(): 
     if event.type == pygame.QUIT: 
       sys.exit(0) 
     else: 
       print event