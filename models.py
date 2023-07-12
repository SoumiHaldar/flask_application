from app import db
from app import app
from datetime import datetime


class Task(db.Model):
    # def test_connection(self):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    date=db.Column(db.Date,nullable=False)
        # return id, title, date
        
    def __repr__(self):
            return f'{self.title} created on {self.date}'
        






# After models.py is created, stop the server, go to cmd(anaconda here),go to the folder, type python (enter)
# type the followings to get a db
#  from app import db,app
# app.app_context().push()
# db.create_all()
# from models import Task
# from datetime import datetime
# t=Task(title='xyz',date=datetime.utcnow())
# db.session.add(t)
# db.session.commit()
# tasks=Task.query.all()