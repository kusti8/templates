from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import werkzeug
# http://flask-restful.readthedocs.io/en/0.3.5/quickstart.html

app = Flask(__name__)
api = Api(app)

class UploadFile(Resource):
#    def put(self):
#        with open('test.jpg', 'wb') as f:
#            f.write(request.stream.read())
#        return {'It': 'Worked'}

    def post(self):
        request.files['file'].save('test.jpg')
        return {'It': 'Worked'}

api.add_resource(UploadFile, '/upload')

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
