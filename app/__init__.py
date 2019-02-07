from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors
# Initializing application
app = Flask(__name__,instance_relative_config = True)
# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

# Registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from app import app