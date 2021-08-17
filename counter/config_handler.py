from os.path import exists as file_exists
# from yaml import safe_load

yaml_default_config = """
---
  counter_file_path: 'counter/counter_file.txt'
  counter_file_text_structure: 'Deaths: {death_count}'

  flask_port: 5000
"""

default_config = {'counter_file_path': 'counter/counter_file.txt',
'counter_file_text_structure': 'Deaths: {death_count}',
'flask_port': 5000}


def if_exists(config_path, default_config):
  """
  Function that makes a config file if there is none at the specified path
  """
  if not file_exists(config_path):
    with open(config_path, 'w') as config_file:
      # YAML implementation: config_file.write(default_config)
      config_file.write(str(default_config))
  return

def load_config(config_path):
  """
  Function that loads and returns config
  
  Atribures:
    config_path: Path to the config file
  
  Returns:
    config(dict): Dictionary of the configuration(?)
  """
  with open(config_path, 'r') as config_file:
    # YAML implementation: config = safe_load(config_file)
    config = config_file.read()
  return config

# validate config() ?
