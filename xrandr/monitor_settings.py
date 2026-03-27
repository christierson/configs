import subprocess
import json

# from settings.settings import Settings

# from settings.settings_manager import SettingsManager

EDID_PATH = "xrandr/edids.json"

CONFIG_PATH = "xrandr/setup-"


PARSE_PREFIX = "$monitor_"


class MonitorSettings:

    def __init__(self):
        with open(EDID_PATH, "r") as f:
            edids = json.load(f)
        self.edid_map: dict[str, str] = edids
        self.load()
        self.apply()

    def load(self):
        output = subprocess.run(["xrandr", "--prop"], capture_output=True, text=True)
        monitors = {}

        prev_monitor = None
        for part in output.stdout.split(" connected "):
            monitor = part.split("\n")[-1]
            if prev_monitor is not None and monitor != prev_monitor:
                edid = part.split("EDID:")[-1]
                edid = "".join(edid.split()[:16])
                monitors[prev_monitor] = edid

            prev_monitor = monitor

        self.monitors = {
            self.edid_map.get(edid, "unknown"): monitor
            for monitor, edid in monitors.items()
        }

        if len(self.monitors) == 1:
            self.mode = "laptop"
        elif len(self.monitors) == 3:
            self.mode = "home"
        elif len(self.monitors) == 4:
            self.mode = "office"
        self.settings = self.setup()
        self.command = self.assemble_xrandr_command()

    def setup(self):
        if not self.mode:
            return {}

        with open(CONFIG_PATH + self.mode + ".json", "r") as f:
            setup = json.load(f)

        return {self.monitors[key]: settings for key, settings in setup.items()}

    def apply(self):
        subprocess.run(self.command.split())

    def assemble_xrandr_command(self):
        command = "xrandr"
        for monitor, settings in self.settings.items():

            command += f" --output {monitor}"

            for key, value in settings.items():
                command += f" --{key} {value}"
        return command

    def parse_monitors(self, string):
        for monitor, name in self.monitors.items():
            string = string.replace(f"{PARSE_PREFIX}{monitor}", name)
        return string

    def exception_command(self, message):
        return f"echo '{message}'"
