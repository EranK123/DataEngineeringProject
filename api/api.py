from dotenv import load_dotenv
import os

load_dotenv()
from flask import Flask, jsonify
from models import db, Area, CaseDetails, CaseRelation, CrimeDescription, Victim, Weapon


def create_app():
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
            weapon_data = {
                'weapon_used_cd': weapon.weapon_used_cd,
                'weapon_desc': weapon.weapon_desc,
                'dr_no': weapon.dr_no
            }
            weapons_list.append(weapon_data)
        return jsonify({'weapons': weapons_list})

    @app.route('/api/victims', methods=['GET'])
    def get_victims():
        victims = Victim.query.all()
        victims_list = []
        for victim in victims:
            victim_data = {
                'victid': victim.victid,
                'vict_age': victim.vict_age,
                'vict_sex': victim.vict_sex,
                'vict_descent': victim.vict_descent,
                'dr_no': victim.dr_no
            }
            victims_list.append(victim_data)
        return jsonify({'victims': victims_list})

    @app.route('/api/crime_description', methods=['GET'])
    def get_crime_descriptions():
        crime_descriptions = CrimeDescription.query.all()
        crime_descriptions_list = []
        for crime_description in crime_descriptions:
            crime_description_data = {
                'crm_cd': crime_description.crm_cd,
                'crm_cd_desc': crime_description.crm_cd_desc,
                'dr_no': crime_description.dr_no
            }
            crime_descriptions_list.append(crime_description_data)
        return jsonify({'crime_descriptions': crime_descriptions_list})

    @app.route('/api/areas', methods=['GET'])
    def get_areas():
        areas = Area.query.all()
        area_list = []
        for area in areas:
            area_data = {
                'area': area.area,
                'area_name': area.area_name,
                'rpt_dist_no': area.rpt_dist_no,
                'dr_no': area.dr_no
            }
            area_list.append(area_data)
        return jsonify({'areas': area_list})

    @app.route('/api/case_details', methods=['GET'])
    def get_case_details():
        case_details = CaseDetails.query.all()
        case_details_list = []
        for case_detail in case_details:
            case_detail_data = {
                'dr_no': case_detail.dr_no,
                'date_occ': case_detail.date_occ,
                'time_occ': case_detail.time_occ,
                'mocodes': case_detail.mocodes,
                'location': case_detail.location,
                'lat': case_detail.lat,
                'lon': case_detail.lon
            }
            case_details_list.append(case_detail_data)
        return jsonify({'case_details': case_details_list})

    @app.route('/api/case_relation', methods=['GET'])
    def get_case_relations():
        case_relations = CaseRelation.query.all()
        case_relations_list = []
        for case_relation in case_relations:
            case_relation_data = {
                'dr_no': case_relation.dr_no,
                'victid': case_relation.victid,
                'area': case_relation.area,
                'crm_cd': case_relation.crm_cd,
                'weapon_used_cd': case_relation.weapon_used_cd
            }
            case_relations_list.append(case_relation_data)
        return jsonify({'case_relations': case_relations_list})

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
