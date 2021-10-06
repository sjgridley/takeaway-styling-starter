from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up configuration settings for connection to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///takeaway.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# Used for demonstration purposes - DO NOT USE IN PRODUCTION
app.config['SECRET-KEY'] = 'this-is-a-secret' 

from app import routes, models

@app.cli.command('init-db')
def init_db():
    # Delete and remake the database 
    db.drop_all()
    db.create_all()

    # Add some sample data for different takeaway items

    hot_chips = models.Item (
        name = 'Hot chips',
        price_cents = 400,
        delivery_available = True
    )
    db.session.add(hot_chips)

    burger = models.Item (
        name = 'Burger',
        price_cents = 800,
        delivery_available = True
    )
    db.session.add(burger)

    fish = models.Item (
        name = 'Fish of the day',
        price_cents = 1000,
        delivery_available = False
    )
    db.session.add(fish)

    # Save the changes to the database
    db.session.commit()

