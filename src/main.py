"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, People
#from models import Person
user = [{
    "id":"0",
    "name":"Pedro",
    "dni":"222222222",},

{   "id":"1",
    "name":"Maria",
    "dni":"111111111",},
{
    "id":"2",
    "name":"Carlos",
    "dni":"333333333",},]

favoritos = [ {
"id":"0",
"name":"Pedro",
"name": "R2-D2",
"name": "Alderaan",
},

{
 "id":"1",
 "name":"Maria",
 "name": "Leia Organa",
 "name": "Endor",  

},
{"id":"2",
"name":"Carlos",
"name": "Beru Whitesun lars",
"name": "Alderaan",},]


people = [{
    "id":"0",
    "name": "R2-D2",
	"height": "96",},

    {
    "id":"1",
    "name": "Leia Organa",
	"height": "150",},

    {
    "id":"2",
    "name": "Beru Whitesun lars",
	"height": "165",},]

planet = [{
    "id":"0",
    "name": "Alderaan",
},
{
    "id":"1",
    "name": "Endor",
	}]

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def user_list():
    user = User.query.all()
    result = []  
    for user in user:
        result.append(user.serialize())

    response_body = {
        "msg": "lista"
    
    }

    return jsonify(result), 200








@app.route('/user/favoritos', methods=['GET'])
def userFav():
     response_body = {
     "msg": "lista favoritos",
     "results": favoritos
 }

     return jsonify(response_body), 200
  

@app.route('/people', methods=['GET'])
def people_list():
    people = People.query.all()
    result = []  
    for people in people:
        result.append(people.serialize())       

    response_body = {
        "msg": "lista"
    
    }

    return jsonify(result), 200


@app.route('/people/<int:id>', methods=['GET'])
def one_person(id):
    people = People.query.get(1)
    people = People.query.filter_by(id=1).one()
    people = People.serialize()
    response_body = {
    "get people"}
   


    return jsonify(result), 200

@app.route('/planets', methods=['GET'])
def planet_list():
    planets = Planet.query.all()
    result = []  
    for planet in planets:
        result.append(planet.serialize())         

    response_body = {
        "msg": "lista"
    
    }

    return jsonify(result), 200

@app.route('/planet/<int:id>', methods=['GET'])
def one_planet(id):
    planet = Planet.query.get(1)
    planet = Planet.query.filter_by(id=1).one()
    planet = planet.serialize()
    response_body = {
        "get planet"
    }


    return jsonify(result), 200

@app.route('/people', methods=['POST'])
def add_people():
   data = request.data
   data = json.loads(data)

   people = people(name = data["name"],id = data["id"])
   db.session.add(people)
   db.session.commit()
   response_body = {
      "msg": "Añadiendo personaje"

   },
   return jsonify(result), 200


@app.route('/people', methods=['DELETE'])
def del_people():
   data = request.data
   data = json.loads(data)

   people = people(name = data["name"],id = data["id"])
   db.session.delete(people)
   db.session.commit()
   
   
   response_body = {
      "msg": "Borrando personaje"

   },
   return jsonify(people), 200


@app.route('/planet', methods=['POST'])
def add_planet():
   data = request.data
   data = json.loads(data)

   planet = planet(name = data["name"],id = data["id"])
   db.session.add(planet)
   db.session.commit()
   response_body = {
      "msg": "Añadiendo planeta"

   },
   return jsonify(planet), 200


@app.route('/planet', methods=['DELETE'])
def del_planet():
   data = request.data
   data = json.loads(data)

   planet = planet(name = data["name"],id = data["id"])
   db.session.delete(planet)
   db.session.commit()
  
   response_body = {
      "msg": "borrando planeta"

   },
   return jsonify(planet), 200







# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
