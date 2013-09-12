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
        # TODO: add validations for missing or incomplete .ini
        config.read('pymulator.ini')

    def build_settings(self, settings):
        settings.add_json_panel('Pymulator', self.config, 'settings.json')

    def build(self):
        self.simulator = Simulator()
        self.simulator.random_list(self.config.getdefaultint('pymulator', 'reqs', 15))
        self.simulator.add_random_pf(self.config.getdefaultint('pymulator', 'pf', 3))
        # self.simulator.requirements = [-5, 15, 40, 65, 20, -35, 400, -511, 380, 12, 500]
        # self.simulator.add_random_pf(3)

    def on_config_change(self, config, section, key, value):
        # TODO: change self.simulator.x to use kivy properties
        # set max, min and validations
        if config is not self.config:
            return
        if key == 'dir':
            self.simulator.direction = value
        elif (key == 'reqs'):
            self.simulator.random_list(int(value))
            self.simulator.add_random_pf(self.config.getdefaultint('pymulator', 'pf', 3))
        elif key == 'init_pos': 
            self.simulator.init_pos = int(value)
        elif key == 'pf':
            self.simulator.random_list(self.config.getdefaultint('pymulator', 'reqs', 15))
            self.simulator.add_random_pf(int(value))


if __name__ == '__main__':
    PymulatorApp().run()
