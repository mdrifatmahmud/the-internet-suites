import os
import yaml
import json

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def load_test_data():
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "test_data.json")
    with open(data_path, "r") as file:
        return json.load(file)

def assets_path(filename):
    return os.path.join(os.path.dirname(__file__), "..", "assets", filename)
// Added helper note for maintainers
