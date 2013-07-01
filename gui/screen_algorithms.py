import os
import sys
import pygame
from pygame.locals import *
from graphic import Graphic


class ScreenAlgorithms:

    """Class that handle the graphics section of the main screen"""
    def __init__(self, size, bkg_colour, simulation):
        # self.size = size
        self.width = size[0]
        self.height = size[1]
        self.graphic_screen = pygame.Surface(size)
        self.graphic_screen.fill(bkg_colour)
        self.bkg_colour = bkg_colour
        self.graphic = Graphic((int(self.width*1/5), 0, int(self.width*4/5), int(self.height*5/6)), (100,100,100))
        self.simulation = simulation
        # just for debuggin purpose. Uncoment to see the size of the surface
        #pygame.draw.rect(self.graphic_screen,(0,0,0),(0,0,self.size[0],self.size[1]),1)

    def __calculate_coordinates(self, requirements):
        reqs_quantity = 0
        for reqs in requirements:
            if reqs:
                reqs_quantity += len(reqs)
        print requirements
        coordinates = ([],[],[])
        # height of the graphic
        y_axis = self.graphic.height - 2* self.graphic.padding
        step = int(y_axis / reqs_quantity)
        i = self.graphic.padding
        for x in range(len(requirements)):
            if requirements[x]:
                for req in requirements[x]:
                    coordinate = ((req + (self.graphic.width - self.simulation.max_tracks+1)/2), i)
                    i += step
                    coordinates[x].append(coordinate)
        print coordinates
        return coordinates


            
            

    def print_graphic(self, list_reqs):
        coors = self.graphic.draw_grid(self.simulation.max_tracks+1, 50)
        self.graphic.label_grid(50, coors)
        self.graphic.draw_graphic(self.__calculate_coordinates(list_reqs))
        #self.graphic_screen.blit(self.graphic.graphic_sfc, (self.graphic.ax_x, self.graphic.ax_y))

    def print_leyends(self, algorithm='Algoritmo', movements='movs', direction="derOizq"):
        if direction:
            directiontxt = 'Derecha'
        else:
            directiontxt = 'Izquierda'
        leyend = 'Metodo:' + algorithm + '     Movimientos: ' + \
             movements + '     Direccion: ' + directiontxt
        pygame.font.init()
        # Let's make the font obj match the space available
        font_size = 100
        leyend_Font = pygame.font.SysFont(None,font_size)
        while ((leyend_Font.size(leyend)[1] > self.height / 4) or (leyend_Font.size(leyend)[0] > self.width * 3/4)):
            font_size -= 10
            leyend_Font = pygame.font.SysFont(None,font_size)

        # Now make the Surface with the font
        leyend_surface = leyend_Font.render(leyend, True, (0, 0, 0))
        #center the surface in the available space
        rect_sfc = leyend_surface.get_rect()
        rect_sfc[1] = 3* self.height/4 + (self.height/4 - leyend_surface.get_height()) /2
        rect_sfc[0] = (3* self.width /4 - leyend_surface.get_width())/2

        #Finally we blit the surface with de centered coordinates 
        self.graphic_screen.blit(leyend_surface, rect_sfc)

        return rect_sfc

    def print_reqs_attended(self):
        pygame.font.init()
        txt = pygame.font.SysFont(None,40)
        txt_sfc = txt.render("Req. Atendidos",True,(0,0,0))
        self.graphic_screen.blit(txt_sfc,((3*self.size[0]/4+(self.size[0]/4 - txt_sfc.get_width())/2),0))
        req_txt = pygame.font.SysFont(None,25)
        i=txt_sfc.get_height()
        for element in self.simulation.algorithm.attended:
            req_sfc = req_txt.render(str(element),True,(0,0,0))
            self.graphic_screen.blit(req_sfc,((3*self.size[0]/4+(self.size[0]/4 - txt_sfc.get_width())/2),i))
            i+=req_sfc.get_height()


