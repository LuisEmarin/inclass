from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from flask_migrate import Migrate, migrate
from .models import db, login_manager,ma
from flask_cors import CORS



# istantiating a new flask app
app = Flask(__name__)
app.config.from_object(Config)

#  registering blueprints tot use within the scope of our whole app
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)
# instantiating db within the scop of our app
db.init_app(app)
# instantiating login_manager within the scope of this app
login_manager.init_app(app)

# instantiating marshmallow
ma.init_app(app)
#specifies what page to load for protected routes when a user is not logged in
login_manager.login_view = 'auth.signin'

# giving flask migrae access to our 
migrate = Migrate(app,db)

CORS(app)
