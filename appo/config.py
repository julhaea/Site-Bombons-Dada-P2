import os
from appo import app

SECRET_KEY = 'minhachave'
SQLALCHEMY_DATABASE_URI = 'sqlite:///bombonsdada.db'  # Caminho para o banco de dados SQLite
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa o rastreamento de modificações para economizar recursos

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')