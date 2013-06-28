import os
import sys
import pygame
from pygame.locals import *
from graphic import Graphic


class Graphics:

    """Class that handle the graphics section of the main screen"""
    def __init__(self, size, bkg_colour):
        self.size = size
        self.graphic_screen = pygame.Surface(size)
        self.graphic_screen.fill(bkg_colour)
        self.bkg_colour = bkg_colour
        # just for debuggin purpose. Uncoment to see the size of the surface
        #pygame.draw.rect(self.graphic_screen,(0,0,0),(0,0,self.size[0],self.size[1]),1)

    def __calculate_coordinates__(self,requirements):
        reqs_quantity = len(requirements)
        # height of the graphic
        y_axis = 3 * self.size[1] / 4 - 20
        step = int(y_axis / reqs_quantity)
        coordinates = []
        i = 20
        for element in requirements:
            coordinate = (element+128,i)
            i += step
            coordinates.append(coordinate)
        return coordinates

    def print_graphic(self, coordinates=(0,0),requirements = [34,65,500,456,321,46,34,511,453,0,34,54,234,76,455,341]):
        graphic = Graphic((3 * self.size[
                          0] / 4, 3 * self.size[1] / 4), self.bkg_colour)

        coors = graphic.make_grid(512,y_coor=20, hspacing = 50)
        graphic.label_grid(50, coors)
        graphic.draw_graphic(self.__calculate_coordinates__(requirements))
        self.graphic_screen.blit(graphic.graphic_sfc, coordinates)

    def print_leyends(self, algorithm='Algoritmo', movements='movs', direction="derOizq"):
        if direction:
            directiontxt = 'Derecha'
        else:
            directiontxt = 'Izquierda'
        leyend = 'Metodo:' + algorithm + '     Movimientos: ' + \
             movements + '     Direccion: ' + directiontxt
        pygame.font.init()
        # Let's make the font obj matching the space available
        font_size = 100
        leyend_Font = pygame.font.SysFont(None,font_size)
        while ((leyend_Font.size(leyend)[1] > self.size[1] / 4)or(leyend_Font.size(leyend)[0] > 3*self.size[0]/4)):
            font_size -= 10
            leyend_Font = pygame.font.SysFont(None,font_size)

        # Now make the Surface with the font
        leyend_surface = leyend_Font.render(leyend, True, (0, 0, 0))
        #center the surface in the available space
        rect_sfc = leyend_surface.get_rect()
        rect_sfc[1] = 3* self.size[1]/4 + (self.size[1]/4 - leyend_surface.get_height()) /2
        rect_sfc[0] = (3* self.size[0] /4 - leyend_surface.get_width())/2

        #Finally we blit the surface with de centered coordinates 
        self.graphic_screen.blit(leyend_surface, rect_sfc)

        return rect_sfc

    def print_reqs_attended(self,list=[34,65,500,456,321,46,34,511,453,0,34,54,234,76,455,341]):
        pygame.font.init()
        txt = pygame.font.SysFont(None,40)
        txt_sfc = txt.render("Req. Atendidos",True,(0,0,0))
        self.graphic_screen.blit(txt_sfc,((3*self.size[0]/4+(self.size[0]/4 - txt_sfc.get_width())/2),0))
        req_txt = pygame.font.SysFont(None,25)
        i=txt_sfc.get_height()
        for element in list:
            req_sfc = req_txt.render(str(element),True,(0,0,0))
            self.graphic_screen.blit(req_sfc,((3*self.size[0]/4+(self.size[0]/4 - txt_sfc.get_width())/2),i))
            i+=req_sfc.get_height()


