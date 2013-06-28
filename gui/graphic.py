import os
import sys
import pygame
from pygame.locals import *


class Graphic():

    def __init__(self, size, bkg_colour):
        self.graphic_sfc = pygame.Surface(size)
        self.graphic_sfc.fill(bkg_colour)
        self.size = size
		#just for debuggin purpose. Uncoment to see the size of the surface
        #pygame.draw.rect(self.graphic_sfc,(0,0,0),(0,0,size[0],size[1]),1)

    def make_grid(self, width ,x_coor=0,y_coor=0, hspacing=0, vspacing=0, gridColour=(0, 0, 0),center = True):
        #if Center = True grid will be x centered
        if center:
        	x_coor = (self.size[0] - width) / 2
        rect = (x_coor, y_coor, width,
                self.size[1] - y_coor - 1)
        # Let's draw the contour of the graphic
        pygame.draw.rect(self.graphic_sfc, gridColour, rect, 2)
        # Now the horizontal lines
        if hspacing != 0:
            for i in range(hspacing, width, hspacing):
                pygame.draw.aaline(self.graphic_sfc, gridColour, (
                    i + x_coor, y_coor), (i + x_coor, rect[3] + y_coor))
        # Finally vertical lines
        if vspacing != 0:
            for i in range(vspacing, width, vspacing):
                pygame.draw.aaline(self.graphic_sfc, gridColour, (
                    x_coor, y_coor + i), (x_coor + width, y_coor + i))
        return rect

    def label_grid(self, hspacing, grid_coor):
        pygame.font.init()
        for i in range(0,grid_coor[2] , hspacing):
            label = pygame.font.SysFont(None, 20)
            label_sfc = label.render(str(i), True, (0, 0, 0))
            # Neded to center the label to the desired coordinate
            half_width = label_sfc.get_width()/2

            self.graphic_sfc.blit(label_sfc, (grid_coor[0]+i-half_width, 0))

    def draw_graphic(self,coordinates,img=''):
    	"""this function takes the coordinates given by any algorithm and draws them in the grid"""

    	pygame.draw.aalines(self.graphic_sfc,(255,0,0),False,coordinates,True)
    	if img=='':
    		for element in coordinates:
    			pygame.draw.circle(self.graphic_sfc,(0,255,255),element,4)
    	else:
    		image_sfc = pygame.image.load(img)

    		for element in coordinates:
    			self.graphic_sfc.blit(image_sfc,element)
		    				
    