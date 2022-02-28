from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
from figaro_api.resources import account
from figaro_api.resources import alert
from figaro_api.db import db

# This is our app
app = Flask(__name__)
CORS(app)

#@app.route('/')
""" def index() :
    alerts = alert.AlertList.get(alert)
    print(type(alerts))
    return render_template('index.html', title="All the alerts", alerts=alerts)
 """
# Setup the URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_api.db"  # The db is a the root
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
api = Api(app)
db.init_app(app)
# We need to create the database
@app.before_first_request
def create_tables():
    db.create_all()


# Add our enpoints
# This will have the GET and POST
api.add_resource(account.AccountList, "/accounts")
#api.add_resource(unit.UnitList, "/units")
api.add_resource(alert.AlertList, "/alerts")

# This will have the GET and POST
api.add_resource(account.Account, "/accounts/<string:_id>")
#api.add_resource(unit.Unit, "/units/<string:_id>")
#api.add_resource(mall.Mall, "/malls/<string:_id>")
