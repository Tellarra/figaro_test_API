from db import db


class AccountModel(db.Model):
    """
    This class is the Account model
    """
    __tablename__ = "account"

    id_account = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    alerts = db.relationship("AlertModel", lazy="dynamic")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        """
        Return a representation of the model
        """
        return {
            "id_account": self.id_account,
            "username": self.username,
            "alerts": [alert.json() for alert in self.alerts.all()],
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
