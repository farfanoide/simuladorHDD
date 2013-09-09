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


# simulator = Simulator()
# simulator.requirements = [-5, 15, 40, 65, 20, -35, -400, 90, 100]

class PymulatorApp(App):
    use_kivy_settings = False

    def build_config(self, config):
        config.read('pymulator.ini')

    def build_settings(self, settings):
        settings.add_json_panel('Pymulator', self.config, 'settings.json')


if __name__ == '__main__':
    PymulatorApp().run()
