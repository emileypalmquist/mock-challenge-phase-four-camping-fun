#!/usr/bin/env python3

from random import choice as rc, randint

from faker import Faker

from app import app
from models import db, Camper, Activity, Signup

fake = Faker()


def make_campers():

    Camper.query.delete()

    campers = []

    for i in range(20):
        camper = Camper(
            name=fake.name(),
            age=randint(8, 18),
        )
        campers.append(camper)

    db.session.add_all(campers)
    db.session.commit()


def make_activities():

    Activity.query.delete()

    activities = []

    for i in range(20):
        activity = Activity(
            name=fake.job(),
            difficulty=randint(1, 10),
        )
        activities.append(activity)

    db.session.add_all(activities)
    db.session.commit()


def make_signups():

    Signup.query.delete()
    activities = Activity.query.with_entities(Activity.id).all()
    campers = Camper.query.with_entities(Camper.id).all()

    signups = []

    for i in range(20):
        signup = Signup(
            time=randint(0, 23),
            camper_id=rc(campers)[0],
            activity_id=rc(activities)[0]
        )
        signups.append(signup)

    db.session.add_all(signups)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        make_campers()
        make_activities()
        make_signups()
