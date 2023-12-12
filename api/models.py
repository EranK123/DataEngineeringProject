from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Area(db.Model):
    __tablename__ = 'area'
    area = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String)
    rpt_dist_no = db.Column(db.Integer)
    dr_no = db.Column(db.Integer)


class CaseDetails(db.Model):
    __tablename__ = 'case_details'
    dr_no = db.Column(db.Integer, primary_key=True)
    date_occ = db.Column(db.String)
    time_occ = db.Column(db.String)
    mocodes = db.Column(db.String)
    location = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)


class CaseRelation(db.Model):
    __tablename__ = 'case_relation'
    dr_no = db.Column(db.Integer, primary_key=True)
    victid = db.Column(db.Integer)
    area = db.Column(db.Integer)
    crm_cd = db.Column(db.String)
    weapon_used_cd = db.Column(db.String)


class CrimeDescription(db.Model):
    __tablename__ = 'crime_description'
    crm_cd = db.Column(db.String, primary_key=True)
    crm_cd_desc = db.Column(db.String)
    dr_no = db.Column(db.Integer)


class Victim(db.Model):
    __tablename__ = 'victim'
    victid = db.Column(db.Integer, primary_key=True)
    vict_age = db.Column(db.Integer)
    vict_sex = db.Column(db.String)
    vict_descent = db.Column(db.String)
    dr_no = db.Column(db.Integer)


class Weapon(db.Model):
    __tablename__ = 'weapon'
    weapon_used_cd = db.Column(db.String)
    weapon_desc = db.Column(db.String)
    dr_no = db.Column(db.Integer,  primary_key=True)
