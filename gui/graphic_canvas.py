import os
import sys
import pygame
from pygame.locals import *
from base_gui import BaseGui

class GraphicCanvas(BaseGui):

    """Class that handle the graphics section of the main screen"""
    def __init__(self, screen, bkg_colour, simulation):
        ####
        self.screen         = screen
        self.width          = screen.get_width()
        self.height         = screen.get_height()
        self.graphic_screen = pygame.Surface((self.width,self.height))
        self.graphic_screen.fill(bkg_colour)
        self.bkg_colour     = bkg_colour
        self.simulation     = simulation
        #####
        self.graphic = Graphic((int(self.width*1/5), 0, int(self.width*4/5), int(self.height*5/6)), (100,100,100), self.simulation.max_tracks+1)
        self.leyend_sfc = pygame.Surface((int(self.width*4/5),int(self.height) - int(self.height*5/6)))
        self.leyend_sfc.fill(bkg_colour)
        self.graphic_screen.blit(self.leyend_sfc,(0,int(self.height*5/6) ))
        self.selected = False

    def __calculate_coordinates(self, requirements):
        """Calculates coordinates for the graphic according to amount of requirements and height available."""
        
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
                    coordinate = ((req, i))
                    i += step
                    coordinates[x].append(coordinate)
        return coordinates

    def print_canvas(self):
        self.graphic.draw_grid(50)
        self.graphic.label_grid(50) 
        self.graphic.canvas_sfc.blit(self.graphic.graphic_sfc,self.graphic.grid_rect)
        self.graphic_screen.blit(self.graphic.canvas_sfc, (0,0))

    def print_graphic(self, list_reqs):
        self.print_canvas()
        self.graphic.draw_graphic(self.__calculate_coordinates(list_reqs))
        self.graphic_screen.blit(self.graphic.canvas_sfc,(0,0))


    def print_leyends(self, algorithm='Algoritmo', movements='movs', direction="derOizq"):
        self.leyend_sfc.fill((self.bkg_colour))
        if direction:
            directiontxt = 'Derecha'
        else:
            directiontxt = 'Izquierda'
        leyend = 'Metodo:' + algorithm + '     Movimientos: ' + \
            str(movements) + '     Direccion: ' + directiontxt
        pygame.font.init()
        # Let's make the font obj match the space available
        font_size = 500
        leyend_Font = pygame.font.SysFont("ubuntu",font_size)
        while ((leyend_Font.size(leyend)[1] > self.leyend_sfc.get_height()) or (leyend_Font.size(leyend)[0] > self.leyend_sfc.get_width())):
            font_size -= 10
            leyend_Font = pygame.font.SysFont("ubuntu",font_size)

        # Now make the Surface with the font
        txt_surface = leyend_Font.render(leyend, True, (0, 0, 0))
        #center the surface in the available space
        rect_sfc = txt_surface.get_rect()
        print rect_sfc
        rect_sfc[1] =(self.leyend_sfc.get_height() - txt_surface.get_height()) /2
        rect_sfc[0] = (self.leyend_sfc.get_width() - txt_surface.get_width())/2

        #Finally we blit the surface with de centered coordinates 
        self.leyend_sfc.blit(txt_surface, rect_sfc)
        self.graphic_screen.blit(self.leyend_sfc,(0,int(self.height*5/6) ))

        return rect_sfc

    def print_reqs_attended(self):
        pygame.font.init()
        txt = pygame.font.SysFont(None,40)
        txt_sfc = txt.render("Req. Atendidos",True,(0,0,0))
        self.graphic_screen.blit(txt_sfc,((3*self.width[0]/4+(self.width[0]/4 - txt_sfc.get_width())/2),0))
        req_txt = pygame.font.SysFont(None,25)
        i=txt_sfc.get_height()
        for element in self.simulation.algorithm.attended:
            req_sfc = req_txt.render(str(element),True,(0,0,0))
            self.graphic_screen.blit(req_sfc,((3*self.width[0]/4+(self.width[0]/4 - txt_sfc.get_width())/2),i))
            i+=req_sfc.get_height()