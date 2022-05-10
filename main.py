import json
from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Response, jsonify, flash, request

#getting all restaurants data
@app.route('/api/restaurants', methods=['GET', 'POST'])
def list_restaurants():
    
    if request.method == 'POST':
        data = request.json
        res = mongo.write('restaurants', data)
    else:
        res = mongo.read('restaurants')
    
    return Response(response=json.dumps(res),
            status=200,
            mimetype='application/json')
    
#for adding menu item and getting menu for a specific restaurant
@app.route('/api/restaurants/<id>/menu/', methods=['GET','POST'])
def restaurant_menu(id):
    
    if request.method == 'POST':
        data = request.json
        res = mongo.update('restaurants',{"id": id},  data)
    else:
        res = mongo.read('restaurants', {"id": id})[0].get('menu', None)
    
    return Response(response=json.dumps(res),
            status=200,
            mimetype='application/json')


if __name__ == "__main__":
    app.run()