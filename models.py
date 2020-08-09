from sqlalchemy.testing.config import db
from sqlalchemy.dialects.mysql import JSON
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#


def setup(app):
    app.config.from_object("config")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    return db

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#


class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(120))
    lanme = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    email = db.Column(db.String(120))
    enrollment = db.relationship(
        "Enrollment", backref="student", cascade="all,delete", lazy=True)


class Course(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(120))
    duration = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    enrollment = db.relationship(
        "Enrollment", backref="subject", cascade="all,delete", lazy=True)


class Instructor(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lanme = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    email = db.Column(db.String(120))
    enrollment = db.relationship(
        "Enrollment", backref="teacher", cascade="all,delete", lazy=True)


class Enrollment(db.Model):
    __tablename__ = "Enrollment"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructor.id"), nullable=False)
