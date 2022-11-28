from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    dni = db.Column(db.Integer, unique=False, nullable=False)
    

    def __repr__(self):
       return self.name #user1

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
    
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)


    def __repr__(self):
        return self.name #people1

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return self.name #Planeta1

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
    
            # do not serialize the password, its a security breach
        }
