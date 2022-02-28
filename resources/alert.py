from flask_restful import Resource, reqparse
from figaro_api.models import alert_model


class Alert(Resource):
    """
    This class can :
    - Get an alert which is in the database
    - Delete an alert
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
        "price_min", type=float, required=True, help="Every alert needs a minimum price"
    )
    parser.add_argument(
        "price_max", type=float, required=True, help="Every alert needs a maximum price"
    )
    parser.add_argument(
        "account_id", type=int, required=True, help="Every alert needs an account id"
    )

    def get(self, _id):
        alert = alert_model.AlertModel.find_by_id(_id)

        if alert:
            return alert.json()
        return {"message": "Alert not found"}, 404

    def delete(self, _id):
        """
        This method delete an alert
        """
        alert = alert_model.AlertModel.find_by_id(_id)

        if alert:
            alert.delete_from_db()

        return {"message": "Alert deleted"}

class AlertList(Resource):
    """
    This class can :
    - Get all the alerts which are in the database
    - Create an alert
    """

    def get(self):
        # We get all the items
        # return {'item' : list(map(lambda x: x.json(), ItemModel.query.all()))} --> Only if not all python
        return {"alerts": [alert.json() for alert in alert_model.AlertModel.query.all()]}

    def post(self):
        # We want to check for errors first
        data = Alert.parser.parse_args()

        alert = alert_model.AlertModel(**data)

        try:
            alert.save_to_db()
        except:
            return {
                "message": "An error ocurred inserting the alert."
            }, 500  # Internal server error

        return alert.json(), 201  # WHEN CREATED