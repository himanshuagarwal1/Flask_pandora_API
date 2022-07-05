from flask import Flask, jsonify
from flask_restful import Api
from data import db
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions




app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False





@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

from endpoints.company import CompanyResource
from endpoints.friends import PeopleResource2
from endpoints.People import PeopleResource

api.add_resource(PeopleResource, '/people/<string:first>&<string:last>')
api.add_resource(PeopleResource2, '/peopletwo/<string:name0>&<string:name01>')
api.add_resource(CompanyResource, '/company/<string:name0>')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
