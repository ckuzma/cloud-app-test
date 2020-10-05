import datetime

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hub(Resource):
    def get(self):
        return {
            'hello': 'world',
            'time': str(datetime.datetime.now())
            }

api.add_resource(Hub, '/')

if __name__ == '__main__':
    app.run(debug=True)