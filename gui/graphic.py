import os
import sys
import pygame
from pygame.locals import *


class Graphic():

    def __init__(self, rect, bkg_colour, grid_width, pad=20):
        self.bkg_colour = bkg_colour
        self.rect = rect
        self.ax_x = rect[0]
        self.ax_y = rect[1]
        self.width = rect[2]
        self.height = rect[3]
        self.padding = pad
        self.canvas_sfc = pygame.Surface((self.width, self.height))
        self.canvas_sfc.fill(self.bkg_colour)
        x_coor = (self.width - grid_width) / 2
        self.grid_rect = (x_coor, self.padding, grid_width,
                self.height - 2 * self.padding - 1)
        self.graphic_sfc = pygame.Surface((self.grid_rect[2], self.grid_rect[3]))

        #TODO: LLENAR CON TRANSPARENCIA
        self.graphic_sfc.fill(self.bkg_colour)
        #self.graphic_sfc.set_colorkey(self.bkg_colour)
        self.canvas_sfc.blit(self.graphic_sfc, (self.grid_rect[0],self.grid_rect[1]))

        #just for debuggin purpose. Uncoment to see the size of the surface
        #pygame.draw.rect(self.canvas_sfc,(0,0,0),rect,1)

    def draw_grid(self, hspacing=0, vspacing=0, gridColour=(0, 0, 0)):
        # Let's draw the contour of the graphic
        pygame.draw.rect(self.canvas_sfc, gridColour, self.grid_rect, 2)
        # Now the horizontal lines
        if hspacing:
            for i in range(hspacing, self.grid_rect[2], hspacing):
                pygame.draw.aaline(self.canvas_sfc, gridColour, (
                    i + self.grid_rect[0], self.padding), (i + self.grid_rect[0], self.height - self.padding))
        # Finally vertical lines
        if vspacing:
            for i in range(vspacing, self.grid_rect[2], vspacing):
                pygame.draw.aaline(self.canvas_sfc, gridColour, (
                    self.padding, self.padding + i), (self.padding + self.grid_rect[0], self.padding + i))

    def label_grid(self, hspacing):
        pygame.font.init()
        grid_ax_x   = self.grid_rect[0] 
        grid_ax_y   = self.grid_rect[1]
        grid_width  = self.grid_rect[2]
        grid_height = self.grid_rect[3]
        for i in range(0, grid_width, hspacing):
            label = pygame.font.SysFont(None, 20)
            label_sfc = label.render(str(i), True, (0, 0, 0))
            # Needed to center the label to the desired coordinate
            half_width = label_sfc.get_width()/2
            self.canvas_sfc.blit(label_sfc, (grid_ax_x + i - half_width, 0))


    def draw_graphic(self, coordinates, img=''):
        """this function takes the coordinates given by any algorithm and draws them in the grid"""
        self.graphic_sfc.fill(self.bkg_colour)
        #self.graphic_sfc.set_colorkey(self.bkg_colour)
        #self.canvas_sfc.blit(self.graphic_sfc,(self.grid_rect[0],self.grid_rect[1]))
        print coordinates
        for x in range(len(coordinates)):
            if coordinates[x]:
                try:
                    if x:
                        pygame.draw.aalines(self.graphic_sfc,(0,0,255),False,coordinates[x],True)
                        if coordinates[x-1] and x == 1:
                            pygame.draw.aaline(self.graphic_sfc,(0,0,255),coordinates[x-1][-1],coordinates[x][0],True)
                    else:
                        pygame.draw.aalines(self.graphic_sfc,(255,0,0),False,coordinates[x],True)
                except ValueError:
                    try:
                        if x:
                            pygame.draw.aaline(self.graphic_sfc,(0,0,255),coordinates[x][-1],coordinates[x+1][0],True)
                        else:
                            pygame.draw.aaline(self.graphic_sfc,(255,0,0),coordinates[x][-1],coordinates[x+1][0],True)
                    except IndexError:
                        pass
                if not img:
                    for element in coordinates[x]:
                        if x:
                            pygame.draw.circle(self.graphic_sfc,(0,255,0),element,4)
                        else:
                            # Different colour for page faults
                            pygame.draw.circle(self.graphic_sfc,(255,0,0),element,4)
                else:
                    image_sfc = pygame.image.load(img)
                    for element in coordinates[x]:
                        self.graphic_sfc.blit(image_sfc,element)

        self.canvas_sfc.blit(self.graphic_sfc,(self.grid_rect[0],self.grid_rect[1]))
        pygame.display.update()
            