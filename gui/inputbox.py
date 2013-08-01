from base import BaseGui
import pygame
from pygame.locals import *
class InputBox(BaseGui):

    """Docstring for InputBox"""
    def __init__(self, base_sfc, rect, color):
        super(InputBox, self).__init__(base_sfc, rect)
        self.inputlst = []
        pygame.draw.rect(self, self._fg_color, self.apply_padding(), 1)
        self.update_sfc()


    def __update_line(self, line, line_height, font):
        """Updates a line on its surface and updates line_height"""

        rendered_line = font.render(line, 1, self._fg_color)
        self.blit(rendered_line, (self.get_padding_left() * 2, line_height))
        line_height += rendered_line.get_height() 

        return line_height, rendered_line

    def __display_box(self, message):
        """Creates a surface to represent the input box itself."""

        font   = pygame.font.Font(None, 18)
        line_h = self.get_padding_top() * 2
        self.draw_surround_rect()

        for line in self.inputlst:
            line_h, cl = self.__update_line(line, line_h, font)

        line_h, curr_line = self.__update_line(message, line_h, font)
        if curr_line.get_width() > (self.get_width() - self.get_padding_right() * 4):
            return True
        else:
            return False

    def __get_final_string(self):
        """Concatenates all strings in self.inputlst and returns them as one"""

        final = ""
        if self.inputlst:
            for i in self.inputlst:
                final += i
        return final

    def __convert_to_list(self):
        full_string = self.__get_final_string()
        try:
            numlist = full_string.rsplit(' ')
            full_list = [int(elem) for elem in numlist]
            return full_list
        except ValueError:
            print "mira si seras gato"
            return None

    def __get_key(self):
        while True:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key
            else:
                pass

    def ask(self):

        pygame.font.init()
        current_string = ""
        self.__display_box(current_string)
        while True:
            inkey = self.__get_key()
            if inkey == K_BACKSPACE:
                if current_string:
                    current_string = current_string[0:-1]
                elif self.inputlst:
                    current_string = self.inputlst.pop()
                self.__display_box(current_string)
            elif inkey == K_RETURN:
                self.inputlst.append(current_string)
                break
            elif inkey <= 127:
                current_string += chr(inkey)
                if self.__display_box(current_string):
                    self.inputlst.append(current_string)
                    current_string = ""
            self.update_sfc()
        return self.__convert_to_list()
