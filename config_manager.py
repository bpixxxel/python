import json

class ConfigManager:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        """ Load configuration from a file. """
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def get_config(self, key):
        """ Retrieve a configuration value. """
        return self.config_data.get(key, None)

    def set_config(self, key, value):
        """ Set a configuration value. """
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        """ Save the configuration to a file. """
        with open(self.config_file, 'w') as file:
            json.dump(self.config_data, file, indent=4)

config_manager = ConfigManager()
print(config_manager.get_config('alert_threshold'))
config_manager.set_config('alert_threshold', 5)
