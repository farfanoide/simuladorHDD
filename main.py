import sys
import os
from kivy.app import App
from kivy.uix.settings import Settings, SettingsPanel
from kivy.config import Config, ConfigParser
from simulator import Simulator
from graphic import Graphic

# -----------
# TODO: get these their own place
# -----------
# HELPERS
# -----------
def convert_str_to_list(string):
    full_string = string
    try:
        numlist = full_string.rsplit(' ')
        full_list = [int(elem) for elem in numlist]
        return full_list
    except ValueError:
        print "mira si seras gato, poneme bien la data"
        return None

def load_file(name):
    """ Load data from a file"""
    # TODO: open a file
    try:
        f = open(sys.path(name),'r')
        lines = f.readlines()
        full_list = convert_str_to_list(lines)
        return full_list
    except IOError:
        return None

class PymulatorApp(App):

    use_kivy_settings = False

    def build_config(self, config):
        # TODO: add validations for missing or incomplete .ini
        config.read('pymulator.ini')

    def build_settings(self, settings):
        settings.add_json_panel('Pymulator', self.config, 'settings.json')

    def build(self):
        self.height = self.config.getdefaultint('graphics', 'height', 700)
        self.width = self.config.getdefaultint('graphics', 'width', 800)
        self.simulator = Simulator()
        self.simulator.direction = self.config.getdefaultint('pymulator', 'dir', True)
        self.simulator.init_pos = self.config.getdefaultint('pymulator', 'init_pos', 250)
        self.simulator.random_list(self.config.getdefaultint('pymulator', 'reqs', 15))
        self.simulator.add_random_pf(self.config.getdefaultint('pymulator', 'pf', 3))

    def on_config_change(self, config, section, key, value):
        # TODO: change self.simulator.x to use kivy properties
        # set max, min and validations
        #  also create custom function for every key with validations and stuff
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
        elif key == 'file':
            reqs = load_file(value)
            if reqs:
                self.simulator.requirements = reqs
        elif key == 'req_list':
            reqs = convert_str_to_list(value)
            if reqs:
                self.simulator.requirements = reqs


if __name__ == '__main__':
    PymulatorApp().run()
