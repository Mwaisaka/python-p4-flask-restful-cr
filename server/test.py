from flask import Flask
from flask_restful import Api, Resource

app=Flask(__name__) 
api=Api(app)

class Newsletter(Resource):
    def get(self):
        return {"newsletter": "It's a beautiful 108 out in Austin today"}
    
api.add_resource(Newsletter, '/newsletters')

if __name__ == '__main__':
    app.run(port=5000)