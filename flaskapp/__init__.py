from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

def create_app():    
    app.config['SECRET_KEY'] = 'thisissecretkey'       
    
    from .views import views
    from .auth import auth
    from .products import products_blueprint
    from .db import db_blueprint

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(products_blueprint)
    app.register_blueprint(db_blueprint)


    return app
