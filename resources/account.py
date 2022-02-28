from flask_restful import Resource, reqparse
from figaro_api.models import account_model


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

class UserRegister(Resource):
    def post(self):
        data = parser.parse_args()

        if account_model.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = AccountModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201

    def get(self, _id):
        account = account_model.AccountModel.find_by_id(_id)

        if account:
            return account.json()
        return {"message": "Account not found"}, 404

    def delete(self, _id):
        account = account_model.AccountModel.find_by_id(_id)

        if account:
            account.delete_from_db()

        return {"message": "Account deleted"}

    def put(self, _id):
        data = Account.parser.parse_args()
        account = account_model.AccountModel.find_by_id(_id)

        if account:
            account.name = data["name"]

        try:
            account.save_to_db()
        except:
            return {"message": "There is no account to update with this id"}

        return account.json()


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
