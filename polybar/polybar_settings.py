import subprocess
from settings.settings import Settings
from xrandr.monitor_settings import MonitorSettings


CONFIG_PATH = "polybar/config-"
CONFIG_BASE = "polybar/config-base.ini"
CONFIG_OUT = "polybar/config.ini"
START_SCRIPT = "polybar/startbar-"


TARGET = "/home/clemensc/.config/polybar/config.ini"


class PolybarSettings(Settings):
    def __init__(self, monitor_settings: MonitorSettings):
        if not super().__init__("polybar_settings", monitor_settings):
            return

        self.config_path = f"{CONFIG_PATH}{self.mode}.ini"
        self.start_script = f"{START_SCRIPT}{self.mode}.sh"
        self.load()
        self.apply()

    def load(self):
        with open(CONFIG_BASE, "r") as f:
            config = f.read()
        with open(self.config_path, "r") as f:
            config += f.read()

        config = self.monitor_settings.parse_monitors(config)

        with open(CONFIG_OUT, "w") as f:
            f.write(config)

    def apply(self):
        subprocess.run(["cp", CONFIG_OUT, TARGET])
        subprocess.run(self.start_script.split(" "))

