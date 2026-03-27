import subprocess
from settings.settings import Settings
from xrandr.monitor_settings import MonitorSettings


CONFIG_PATH = "polybar/config-"
CONFIG_BASE = "polybar/config-base.ini"
CONFIG_OUT = "polybar/config.ini"
START_SCRIPT = "polybar/startbar-"


TARGET = "/home/clemensc/.config/polybar/config.ini"


class Nitrogen(Settings):
    def __init__(self, monitor_settings: MonitorSettings):
        if not super().__init__("polybar_settings", monitor_settings):
            return

        self.start_script = "nitrogen --restore"
        self.apply()

    def apply(self):
        subprocess.run(self.start_script.split(" "))
