import yaml
import os

def load_config():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    config_path = os.path.join(project_root, 'config', 'config.yaml')
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    config['app']['log_file'] = os.path.join(project_root, config['app']['log_file'])
    
    return config