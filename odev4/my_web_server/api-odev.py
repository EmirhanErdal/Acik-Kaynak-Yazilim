from flask import Flask, request

from flask_restful import Api, Resource

import pandas as pd

import requests





app = Flask(__name__)

api = Api(app)



class Cats(Resource):

   def get(self,sayi):

       url = "https://meowfacts.herokuapp.com/?count="+ sayi



       resp= requests.get(url)

       data = resp.json()


       return {'data' : data}, 200




api.add_resource(Cats, '/cats/<string:sayi>')





if __name__ == '__main__':

   app.run(host="0.0.0.0", port=6767)

   app.run()