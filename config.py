import os

basedir = os.path.abspath(os.path.dirname(__file__))

# gives us access to this project location in any OS we fing ourselves in
# allows us access to ther folders to be added into project from external sources


class Config:
    
    SECRET_KEY = "You will never guess..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #DECREASES UNNECESSARY OUTPUT IN TERMINAL AS WE USE THE DB




