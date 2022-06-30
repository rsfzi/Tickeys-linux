import configparser
import os
from logger import logger


class Configer():
    """docstring for Configer"""
    def __init__(self, *arg):
        try:
            os.chdir(os.path.dirname(__file__))
        except Exception:
            pass
        self.config_path = os.environ["HOME"] + "/.tickeys/tickeys.conf"
        self.cf = configparser.ConfigParser()
        self.read_config()

    def init_config(self):
        self._style = 'mechanical'
        self._volume = 1.0
        self._pitch = 1.0
        self._lang = 'en_US'
        self._autostart = False
        self.save_config()

    def read_config(self):
        try:
            if not os.path.exists(self.config_path):
                self.init_config()
            else:
                self.cf.read(self.config_path)
                self._volume = self.cf.getfloat('options', 'volume')
                self._pitch = self.cf.getfloat('options', 'pitch')
                self._style = self.cf.get('options', 'style')
                self._autostart = self.cf.get('options', 'autostart')
                self._lang = self.cf.get('options', 'lang')
        except Exception as e:
            self.init_config()
            logger.debug(e)

    def save_config(self):
        if not self.cf.sections():
            self.cf.add_section('options')
        self.cf.set('options', 'volume', self._volume)
        self.cf.set('options', 'pitch', self._pitch)
        self.cf.set('options', 'style', self._style)
        self.cf.set('options', 'lang', self._lang)
        self.cf.set('options', 'autostart', self._autostart)

        with open(self.config_path, 'w') as f:
            self.cf.write(f)

    @property
    def volume(self):
        return self._volume

    @property
    def pitch(self):
        return self._pitch

    @property
    def style(self):
        return self._style

    @property
    def lang(self):
        return self._lang

    @property
    def autostart(self):
        return self._autostart

configer = Configer()
