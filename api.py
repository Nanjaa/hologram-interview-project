from flask_restful import Resource

class Cdr(Resource):
    def post(self):
        return {'hello': 'world'}
