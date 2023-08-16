"""
__init__.py

Date: 08/05/2023

Programmer's name: Suren Tumasyan, Ronny Almahdi

Description: Creates and configures the Flask application

"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

def create_app():
    """Creates and configures the Flask application.
    
    Returns:
        Flask: Configured Flask application instance.
    """
    app.config['SECRET_KEY'] = 'thisissecretkey'       
    
    from .views import views
    from .auth import auth
    from .products import products_blueprint
    from .db import db_blueprint
    from .cart import cart_blueprint
    from .checkout import checkout_blueprint 

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(products_blueprint)
    app.register_blueprint(db_blueprint)
    app.register_blueprint(cart_blueprint)
    app.register_blueprint(checkout_blueprint) 


    return app
