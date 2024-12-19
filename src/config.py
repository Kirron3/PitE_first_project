import yaml
import os

def load_config():
    config_path = os.path.join('project','config', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)