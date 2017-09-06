from flask_sqlalchemy import SQLAlchemy
from app.app import app
from config import config

app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')
db = SQLAlchemy(app)


class Sprint(db.Model):
    __tablename__ = 'sprint'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.DateTime(), unique=False)
    end_date = db.Column(db.DateTime(), unique=False)
    story_points_committed = db.Column(db.Integer, unique=False)
    story_points_finished = db.Column(db.Integer, unique=False)
    cases_inside_sprint = db.Column(db.Integer, unique=False)
    members_amount = db.Column(db.Integer, unique=False)

    def __init__(self, start_date, end_date, story_points_committed, story_points_finished, cases_inside_sprint,
                 members_amount):
        self.start_date = start_date
        self.end_date = end_date
        self.story_points_committed = story_points_committed
        self.story_points_finished = story_points_finished
        self.cases_inside_sprint = cases_inside_sprint
        self.members_amount = members_amount

    def to_dict(self):
        return {'id': self.id, 'start_date': self.start_date, 'end_date': self.end_date,
                'story_points_committed': self.story_points_committed,
                'story_points_finished': self.story_points_finished,
                'cases_inside_sprint': self.cases_inside_sprint, 'members_amount': self.members_amount}

    def save(self):
        db.session.add(self)
        db.session.commit()
