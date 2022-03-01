from flask_restful import Resource, reqparse
from models import account_model


class Account(Resource):
    """
    This class can :
    - Get an account which is in the database
    - Update a new account or return a message
    - Delete an account and their malls
    """

    parser = reqparse.RequestParser()
    parser.add_argument( "username", 
                            type=str, 
                            required=True, 
                            help="This field cannot be left blank"
    )
    parser.add_argument("password",
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )

class AccountList(Resource):
    """
    This class can :
    - Get all the accounts which are in the database
    - Create an account
    """

    def get(self):
        return {"accounts": [account.json() for account in account_model.AccountModel.query.all()]}

    def post(self):
        data = Account.parser.parse_args()
        account = account_model.AccountModel(**data)

        try:
            account.save_to_db()
        except:
            return {
                "message": "An error ocurred inserting the account."
            }, 500  # Internal server error

        return account.json(), 201  # WHEN CREATED
