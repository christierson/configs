from settings.settings_manager import SettingsManager
from xrandr.monitor_settings import MonitorSettings


# class Settings:
#     def __init__(self, key, default_settings: dict = None, s: SettingsManager = None):
#         self.key = key
#         self.default_settings = default_settings
#         self.settings = {}
#         self.s = s

#     def load(self):
#         settings = self.s.get(self.key, self.default_settings)
#         for key, value in self.default_settings.items():
#             if key not in settings:
#                 settings[key] = value
#         self.settings = settings
#         self.save()

#     def save(self):
#         self.s.set(self.key, self.settings)
#         self.s.save()

#     def set(self, key, value):
#         self.settings[key] = value
#         self.save()

#     def apply(self):
#         pass

SETTINGS_PATH = "settings/settings.json"


class Settings:

    def __init__(self, key, monitor_settings: MonitorSettings):
        self.key = key
        self.settings = {}

        if not monitor_settings.mode or not monitor_settings.monitors:
            return False

        self.monitor_settings = monitor_settings
        self.mode = monitor_settings.mode
        self.monitors = monitor_settings.monitors

        return True
