from flask import Blueprint, render_template, session
from flask_login import current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy

from . import app


db_blueprint = Blueprint('db', __name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://sql9635613:aL1s9kYG4G@sql9.freemysqlhosting.net:3306/sql9635613'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
#initialize DB
db = SQLAlchemy(app)
app.app_context().push()

from .modules.models.user_model import Users
from .modules.models.cart_model import Cart

#Testing db by just finding a user and their cart
@db_blueprint.route("/db")
def db_route():
    # THIS CODE WORKS!
        
    # curr_user = db.get_or_404(Users, 5) #5 is the id of the Users (primary key)
    curr_user = Users.query.filter(Users.email == "test@csun.com").first()
    curr_user_cart = Cart.query.filter(Cart.owner_id == curr_user.id).all()
        
    return render_template("testdb.html", user = curr_user, user_cart = curr_user_cart)



