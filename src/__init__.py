import os
import json

def get_config(key):
    config_file = os.path.join(os.path.dirname(__file__), "config.json")
    file = open(config_file, "r")
    config = json.loads(file.read())
    file.close()
    
    if key in config:
        return config[key]
    else:
        raise Exception("Key {} is not found in config.json".format(key))
