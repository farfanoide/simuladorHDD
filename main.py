from kivy.app import App


# from kivy.uix.widget import Widget
# from kivy.uix.screenmanager import ScreenManager
from kivy.uix.settings import Settings, SettingsPanel
from simulator import Simulator
from kivy.config import Config, ConfigParser
from graphic import Graphic




class PymulatorApp(App):

    use_kivy_settings = False

    def build_config(self, config):
        config.read('pymulator.ini')

    def build_settings(self, settings):
        settings.add_json_panel('Pymulator', self.config, 'settings.json')

    def build(self):
        self.simulator = Simulator()
        self.simulator.requirements = [-5, 15, 40, 65, 20, -35, 400, -511, 380, 12, 500]
        # self.simulator.random_list(15)
        # self.simulator.add_random_pf(3)


if __name__ == '__main__':
    PymulatorApp().run()
