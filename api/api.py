from dotenv import load_dotenv
import os
from flask import Flask, jsonify
from models import db, Area, CaseDetails, CaseRelation, CrimeDescription, Victim, Weapon


def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("CRIMES_DB_USER")}:' \
                                            f'{os.getenv("CRIMES_DB_PASSWORD")}@{os.getenv("CRIMES_DB_HOST")}:' \
                                            f'{os.getenv("CRIMES_DB_PORT")}/{os.getenv("CRIMES_DB_DATABASE")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/api/weapons', methods=['GET'])
    def get_weapons():
        weapons = Weapon.query.all()
        weapons_list = []
        for weapon in weapons:
            weapon_dict = weapon.__dict__
            weapon_dict.pop('_sa_instance_state', None)
            weapons_list.append(weapon_dict)
        return jsonify({'weapons': weapons_list})

    @app.route('/api/victims', methods=['GET'])
    def get_victims():
        victims = Victim.query.all()
        victims_list = []
        for victim in victims:
            victim_dict = victim.__dict__
            victim_dict.pop('_sa_instance_state', None)
            victims_list.append(victim_dict)
        return jsonify({'victims': victims_list})

    @app.route('/api/crime_description', methods=['GET'])
    def get_crime_descriptions():
        crime_descriptions = CrimeDescription.query.all()
        crime_descriptions_list = []
        for crime_description in crime_descriptions:
            crime_description_dict = crime_description.__dict__
            crime_description_dict.pop('_sa_instance_state', None)
            crime_descriptions_list.append(crime_description_dict)
        return jsonify({'crime_descriptions': crime_descriptions_list})

    @app.route('/api/areas', methods=['GET'])
    def get_areas():
        areas = Area.query.all()
        area_list = []
        for area in areas:
            area_dict = area.__dict__
            area_dict.pop('_sa_instance_state', None)
            area_list.append(area_dict)
        return jsonify({'areas': area_list})

    @app.route('/api/case_details', methods=['GET'])
    def get_case_details():
        case_details = CaseDetails.query.all()
        case_details_list = []
        for case_detail in case_details:
            case_detail_dict = case_detail.__dict__
            case_detail_dict.pop('_sa_instance_state', None)
            case_details_list.append(case_detail_dict)
        return jsonify({'case_details': case_details_list})

    @app.route('/api/case_relation', methods=['GET'])
    def get_case_relations():
        case_relations = CaseRelation.query.all()
        case_relations_list = []
        for case_relation in case_relations:
            case_relation_dict = case_relation.__dict__
            case_relation_dict.pop('_sa_instance_state', None)
            case_relations_list.append(case_relation_dict)
        return jsonify({'case_relations': case_relations_list})

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
