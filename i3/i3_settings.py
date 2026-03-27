from settings.settings import Settings
from xrandr.monitor_settings import MonitorSettings
import subprocess

CONFIG_PATH = "i3/config-"
CONFIG_BASE = "i3/config-base"
CONFIG_OUT = "i3/config"


TARGET = "/home/clemensc/.config/i3/config"


class I3Settings(Settings):

    def __init__(self, monitor_settings: MonitorSettings):
        if not super().__init__("i3_settings", monitor_settings):
            return

        self.config_path = f"{CONFIG_PATH}{self.mode}"
        self.start_script = "i3-msg restart"
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
