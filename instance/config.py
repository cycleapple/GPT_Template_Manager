import os

# Configuration options
SECRET_KEY = 'replace_with_your_secret_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'blocks.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
