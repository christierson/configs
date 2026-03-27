import os
import json

SETTINGS_PATH = "settings/settings.json"


class SettingsManager:
    def __init__(self):
        if os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, "r") as f:
                settings = json.load(f)
            if settings is not None:
                self.settings = settings
                return

        with open(SETTINGS_PATH, "w") as f:
            json.dump({}, f)
            self.settings = {}

    def save(self):
        with open(SETTINGS_PATH, "w") as f:
            json.dump(self.settings, f, indent=4)

    def set(self, key, value):
        self.settings[key] = value
        self.save()

    def get(self, key, default=None):
        return self.settings.get(key, default)
