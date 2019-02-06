from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
# from flask_appbuilder import Model

class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

# class QIDMapping(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     mes = db.Column(db.Integer)
#     aluguel = db.Column(db.String(75))
#     luz = db.Column(db.String(75))
#     agua = db.Column(db.String(75))
#     telefone = db.Column(db.String(75))