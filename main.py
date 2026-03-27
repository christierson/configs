import os
import json

# SETTINGS_PATH = "settings.json"

# DEFAULT_SETTINGS = {
#     "keyboard_layout": "us",
#     "mode": "office",
#     "touchpad": {
#         "tapping_enabled": 1,
#         "natural_scrolling_enabled": 1,
#         "accel_speed": 0.35,
#     },
# }


# def load():
#     if os.path.exists(SETTINGS_PATH):
#         with open(SETTINGS_PATH, "r") as f:
#             settings = json.load(f)
#     else:
#         with open(SETTINGS_PATH, "w") as f:
#             json.dump(DEFAULT_SETTINGS, f, indent=4)
#         settings = DEFAULT_SETTINGS
#     return settings


# def set(setting, value):
#     settings = load()
#     settings[setting] = value
#     with open(SETTINGS_PATH, "w") as f:
#         json.dump(settings, f, indent=4)


# def initialize():
#     settings = load()


# print(load())
# from settings.settings_manager import SettingsManager
from nitrogen.nitrogen import Nitrogen
from xrandr.monitor_settings import MonitorSettings
from polybar.polybar_settings import PolybarSettings
from i3.i3_settings import I3Settings

# s = SettingsManager()
monitor_settings = MonitorSettings()
i3_settings = I3Settings(monitor_settings)
polybar_settings = PolybarSettings(monitor_settings)
nitrogen = Nitrogen(monitor_settings)

# print(s.settings)
