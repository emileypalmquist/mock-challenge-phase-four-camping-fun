from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Camper, Activity, Signup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


class Campers(Resource):
    def get(self):
        campers = Camper.query.all()
        campers_dict_list = [camper.to_dict(
            rules=('-activities',)) for camper in campers]
        response = make_response(
            campers_dict_list,
            200
        )
        return response

    def post(self):
        data = request.get_json()

        camper = Camper(
            name=data['name'],
            age=data['age']
        )

        db.session.add(camper)
        db.session.commit()

        response = make_response(
            camper.to_dict(),
            201
        )
        return response


api.add_resource(Campers, '/campers')


class CamperById(Resource):
    def get(self, id):
        camper = Camper.query.filter_by(id=id).first()
        if not camper:
            return make_response({
                "error": "Camper not found"
            }, 404)
        response = make_response(
            camper.to_dict(),
            200
        )
        return response


api.add_resource(CamperById, '/campers/<int:id>')


class Activities(Resource):
    def get(self):
        activities = Activity.query.all()
        activities_dict_list = [activity.to_dict() for activity in activities]

        response = make_response(activities_dict_list, 200)
        return response


api.add_resource(Activities, '/activities')


class ActivitiesById(Resource):

    def delete(self, id):
        pass


api.add_resource(ActivitiesById, '/activites')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
