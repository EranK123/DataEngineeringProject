from flask_sqlalchemy import SQLAlchemy
import const

db = SQLAlchemy()


class Area(db.Model):
    __tablename__ = const.TABLE_NAMES['area']
    area = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String)
    rpt_dist_no = db.Column(db.Integer)
    dr_no = db.Column(db.Integer)


class CaseDetails(db.Model):
    __tablename__ = const.TABLE_NAMES['case_details']
    dr_no = db.Column(db.Integer, primary_key=True)
    date_occ = db.Column(db.String)
    time_occ = db.Column(db.String)
    mocodes = db.Column(db.String)
    location = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)


class CaseRelation(db.Model):
    __tablename__ = const.TABLE_NAMES['case_relation']
    dr_no = db.Column(db.Integer, primary_key=True)
    victid = db.Column(db.Integer)
    area = db.Column(db.Integer)
    crm_cd = db.Column(db.String)
    weapon_used_cd = db.Column(db.String)


class CrimeDescription(db.Model):
    __tablename__ = const.TABLE_NAMES['crime_description']
    crm_cd = db.Column(db.String, primary_key=True)
    crm_cd_desc = db.Column(db.String)
    dr_no = db.Column(db.Integer)


class Victim(db.Model):
    __tablename__ = const.TABLE_NAMES['victim']
    victid = db.Column(db.Integer, primary_key=True)
    vict_age = db.Column(db.Integer)
    vict_sex = db.Column(db.String)
    vict_descent = db.Column(db.String)
    dr_no = db.Column(db.Integer)


class Weapon(db.Model):
    __tablename__ = const.TABLE_NAMES['weapon']
    weapon_used_cd = db.Column(db.String)
    weapon_desc = db.Column(db.String)
    dr_no = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return str({
            "dr_no": self.dr_no,
            "weapon_used_cd": self.weapon_used_cd,
            "weapon_desc": self.weapon_desc
        })
