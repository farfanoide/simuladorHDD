from base import BaseGui
class Screen(BaseGui):
    """docstring for Screen"""


    def __init__(self, base_sfc, rect, color, elements=[]):
        super(Screen, self).__init__(base_sfc, rect, color)
        self.elements = elements
        self.selected = False
        self.last_scr = None
        self.next_scr = None

    
    def switch_select(self):
        self.selected = not self.selected
        if self.selected:
            self.update_sfc()
            # self.last_scr.switch_select()

    def set_last_screen(self, last_scr):
        self.last_scr = last_scr
    
    def set_next_screen(self, next_scr):
        self.next_scr = next_scr

    def go_back(self):
        if self.selected:
            self.switch_select()
            self.last_scr.switch_select()
    
    def go_forward(self):
        if self.selected:
            self.switch_select()
            self.next_scr.switch_select()

    def get_menu(self):
        try:
            for elem in self.elements:
                if elem.__class__.__name__ == "Menu":
                    return elem
        except IndexError:
            return None
    
    def get_graphic(self):
        try:
            for elem in self.elements:
                if elem.__class__.__name__ == "Graphic":
                    return elem
        except IndexError:
            return None

