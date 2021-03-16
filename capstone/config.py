import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Database connection string
SQLALCHEMY_DATABASE_URI = 'postgres://yflmtcyphhmyoj:14dabe94206a1760f431e314537033a05f7b5ea2f12656a66266b07ae6565a1c@ec2-54-90-13-87.compute-1.amazonaws.com:5432/d37d3fi5o0hf7h'
# Supress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False