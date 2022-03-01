from sqlalchemy.orm import backref
from db import db


class AlertModel(db.Model):
    """
    This class is the Mall model
    """

    __tablename__ = "alert"

    id_alert = db.Column(db.Integer, primary_key=True)
    name_alert = db.Column(db.String(80))
    creation_date = db.Column(db.DateTime())
    price_min = db.Column(db.Float)
    price_max = db.Column(db.Float)
    city = db.Column(db.String(80))

    # Setting up the foreign key
    username = db.Column(db.Integer, db.ForeignKey("account.username"))
    account = db.relationship(
        "AccountModel", backref=backref("alert", cascade="all, delete")
    )

    def __init__(self, name_alert,price_min, price_max, city, username):
        self.name_alert = name_alert
        self.price_min = price_min
        self.price_max = price_max
        self.city = city
        self.username = username

    def json(self):
        """
        Return a representation of the model
        """
        return {
            "id_alert": self.id_alert,
            "name_alert": self.name_alert,
            "price_min": self.price_min,
            "price_max": self.price_max,
            "city": self.city,
            "username": self.username,
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id_mall=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()