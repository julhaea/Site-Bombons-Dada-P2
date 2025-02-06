import os
from appo import app

SECRET_KEY = 'minhachave'
SQLALCHEMY_DATABASE_URI = 'sqlite:///bombonsdada.db'  # Caminho para o banco de dados SQLite
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa o rastreamento de modificações para economizar recursos

