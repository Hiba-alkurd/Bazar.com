from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api
from flask import request

import json


app = Flask(__name__)
api = Api(app)


@app.route('/getRecommendation', methods=['POST'])
def getRecommendation():
    productID = request.form['productID']
    return ""


@app.route('/getRecommendationForAll', methods=['POST'])
def getRecommendationForAll():
    productIDs = str(request.form['productIDs']).split(',')
    return ""

@app.route("/hello")
def hello():
    # global RS
    # RS.justPrintSomething()
    return {"data": "Welcome to machine learning model APIs!"}


@app.route('/getSentiment', methods=['POST'])
def find_sentiment():
    data = request.json
    return data


@app.route('/process_data', methods=['POST'])
def process_data():
    return "hey you!"
    # return request.data
    # req_data = request.get_json(force=True)
    # return req_data['user1']
    # return request.form['name']
    # return (request.form['user1'])




if __name__ == '__main__':
    app.run(debug=True, port=4040)
