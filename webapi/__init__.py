from flask_restx import Api 

from .todo import api as todo_api

api = Api(
    title='My Web API with Python',
    version='1.0',
    description='Web API Demo with Python'
)

api.add_namespace(todo_api)
