import os
from sqlalchemy import Column, String, Integer, Enum
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_name = "capstone"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()
# setup_db(app)

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app=app
    db.init_app(app)
    migrate = Migrate(app, db)


class Game(db.Model):
    __tablename__ = 'Game'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genres = db.Column(db.ARRAY(db.String))
    rating = db.Column(db.Integer)
    completed = db.Column(db.Boolean, nullable=False, default=False)


    def full(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "genres": self.genres,
            "rating": self.rating
        }
    
    def short(self):
        return {
            "id": self.id,
            "title": self.title
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Character(db.Model):
    __tablename__ = 'Character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    fighting = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    good = db.Column(db.Boolean, nullable=False, default=True)
    game_id = db.Column(db.Integer, db.ForeignKey('Game.id'), nullable=False)

    def full(self):
        return {
            "id": self.id,
            "name": self.name,
            "fighting": self.fighting,
            "intelligence": self.intelligence,
            "good": self.good,
            "game_id": self.game_id
        }

    def short(self):
        return {
            "id": self.id,
            "title": self.name
        }

    def insert(self):
        print("4")
        db.session.add(self)
        print("5")
        db.session.commit()
        print("6")

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()









