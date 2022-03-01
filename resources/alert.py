from flask_restful import Resource, reqparse
from models import alert_model


class Alert(Resource):
    """
    This class can :
    - Get an alert which is in the database
    """

    # Implement a decorator
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name_alert", type=str, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "city", type=str, required=True, help="Every alert needs a city location"
    )
    parser.add_argument(
        "price_min", type=float, required=False
    )
    parser.add_argument(
        "price_max", type=float, required=False
    )
    parser.add_argument(
        "username", type=str, required=True, help="Every alert needs a username"
    )

class AlertList(Resource):
    """
    This class can :
    - Get all the alerts which are in the database
    - Create an alert
    """

    def get(self):
        # We get all the items
        return {"alerts": [alert.json() for alert in alert_model.AlertModel.query.all()]}

    def post(self):
        # We want to check for errors first
        data = Alert.parser.parse_args()

        alert = alert_model.AlertModel(**data)

        if alert.price_min and alert.price_max :
            if alert.price_min > alert.price_max  :
                return {
                    "message": "The minimum price must be lower than the maximum price."
                }

        for character in alert.city:
            if character.isdigit():
                return {
                    "message": "The city name is not valid."

        if not account_model.AccountModel.find_by_username(alert.username) :
            return {
                "message": "The username you entered doesn't exist."
            }

        try:
            alert.save_to_db()
        except:
            return {
                "message": "An error ocurred inserting the alert."
            }, 500  # Internal server error

        return alert.json(), 201  # WHEN CREATED
