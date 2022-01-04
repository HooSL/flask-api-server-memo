from flask import Flask, request
# JWT 사용을 위한 SECRET_KEY 정보가 들어있는 파일 임포트
from config import Config
from flask.json import jsonify
from http import HTTPStatus

from flask_restful import Api

from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config.from_object(Config)

api = Api(app)

api.add_resource(, '/memo')
api.add_resource(, '/memo/<int:recipe_id>')
api.add_resource(, '/memo/<int:recipe_id>/publish')
api.add_resource(, '/user/register')
api.add_resource(, '/user/login')
api.add_resource(, '/user/logout')

if __name__ == "__main__" :
    app.run()