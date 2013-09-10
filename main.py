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


# simulator = Simulator()
# simulator.requirements = [-5, 15, 40, 65, 20, -35, -400, 90, 100]

class Graphic(RelativeLayout):

    """Graphic class to print requirements to canvas"""

    def __init__(self, **kwargs):
        super(Graphic, self).__init__(**kwargs)
        self.draw_grid()

    def draw_grid(self):

        for x in xrange(100, 550, 50):
            with self.canvas:
                Line(points=[x, 0, x, 400], width=1)
            self.add_widget(Label(text=str(x), pos=(x - 350, 200)))


class PymulatorApp(App):

    use_kivy_settings = False

    def build_config(self, config):
        config.read('pymulator.ini')

    def build_settings(self, settings):
        settings.add_json_panel('Pymulator', self.config, 'settings.json')


if __name__ == '__main__':
    PymulatorApp().run()
