from . import config_handler
from flask import Flask


config_path = 'counter/config.yaml'

config_handler.if_exists(config_path, config_handler.default_config)
config_dict = config_handler.load_config(config_path)

app = Flask(__name__)

@app.route('/')
def hello():
  return(str(config_dict))
