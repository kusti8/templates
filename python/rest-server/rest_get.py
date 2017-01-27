from flask import Flask
from flask_restful import Resource, Api
# http://flask-restful.readthedocs.io/en/0.3.5/quickstart.html

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Hi(Resource):
    def get(self, arg):
        return {'arg': arg}
        # Return, value, header: return {'arg': arg}, 200, {'Cus': 'tom header'}

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(HelloWorld, '/hi')
api.add_resource(Hi, '/args/<arg>')

if __name__ == '__main__':
    app.run(debug=True)
