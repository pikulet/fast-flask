from app import db

class Text(db.Model):

    __tablename__ = 'fastflask'

    text_id = db.Column(db.Integer, primary_key=True)
    text_value = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, value):
        self.text_value = value

    def __repr__(self):
        return self.value

    def serialise(self):
        return {
            'value' :   self.value
        }
