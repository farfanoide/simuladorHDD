from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.settings import Settings, SettingsPanel
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.clock import Clock
from simulator import Simulator
from kivy.config import Config, ConfigParser
from kivy.graphics import Line, Rectangle
from kivy.uix.relativelayout import RelativeLayout


class Graphic(RelativeLayout):

    """Graphic class to print requirements to canvas"""

    def __init__(self, **kwargs):
        super(Graphic, self).__init__(**kwargs)
        self.draw_grid()

    def draw_grid(self):

        for x in xrange(100, 550, 50):
            with self.canvas:
                Line(points=[x, 0, x, 400], width=1)
            # TODO: borrar paddings hardcodeados
            self.add_widget(Label(text=str(x), pos=(x - 350, 200)))

    def __calculate_coordinates(self, requirements):
        """Calculates coordinates for the graphic according to amount of requirements and height available."""
        # TODO: hacer esto bien
        # step = self.__calculate_vertical_step(requirements)
        print requirements
        step = 15
        coordinates = ([], [], [])
        i   = 100 #self.get_padding_top()
        pad = 100 #self.get_padding_left()
        for x in range(len(requirements)):
            try:
                for req in requirements[x]:
                    # coordinate = ((req + pad, i))
                    coor = req + pad
                    coordinates[x].append(coor)
                    coordinates[x].append(i)
                    i += step
                    # coordinates[x].append(coor)
            except IndexError:
                pass
        return coordinates

    def draw_lines(self, requirements):
        coordinates = self.__calculate_coordinates(requirements)
        with self.canvas:
            for x in range(len(coordinates)):
                if coordinates[x]:
                    Line(points=coordinates[x], width=1)





class PymulatorApp(App):

    use_kivy_settings = False

    def build_config(self, config):
        config.read('pymulator.ini')

    def build_settings(self, settings):
        settings.add_json_panel('Pymulator', self.config, 'settings.json')

    def build(self):
        self.simulator = Simulator()
        self.simulator.random_list(15)
        self.simulator.add_random_pf(3)


if __name__ == '__main__':
    PymulatorApp().run()
