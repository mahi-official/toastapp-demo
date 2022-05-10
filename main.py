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


	# _json = request.json
	# _name = _json['name']
	# _email = _json['email']
	# _password = _json['pwd']
	# # validate the received values
	# if _name and _email and _password and request.method == 'POST':
	# 	#do not save password as a plain text
	# 	_hashed_password = generate_password_hash(_password)
	# 	# save details
	# 	id = mongo.db.user.insert({'name': _name, 'email': _email, 'pwd': _hashed_password})
	# 	resp = jsonify('User added successfully!')
	# 	resp.status_code = 200
	# 	return resp
	# else:
	# 	return not_found()
		
# @app.route('/users')
# def users():
# 	users = mongo.db.user.find()
# 	resp = dumps(users)
# 	return resp
		
# @app.route('/user/<id>')
# def user(id):
# 	user = mongo.db.user.find_one({'_id': ObjectId(id)})
# 	resp = dumps(user)
# 	return resp

# @app.route('/update', methods=['PUT'])
# def update_user():
# 	_json = request.json
# 	_id = _json['_id']
# 	_name = _json['name']
# 	_email = _json['email']
# 	_password = _json['pwd']		
# 	# validate the received values
# 	if _name and _email and _password and _id and request.method == 'PUT':
# 		#do not save password as a plain text
# 		_hashed_password = generate_password_hash(_password)
# 		# save edits
# 		mongo.db.user.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name': _name, 'email': _email, 'pwd': _hashed_password}})
# 		resp = jsonify('User updated successfully!')
# 		resp.status_code = 200
# 		return resp
# 	else:
# 		return not_found()
		
# @app.route('/delete/<id>', methods=['DELETE'])
# def delete_user(id):
# 	mongo.db.user.delete_one({'_id': ObjectId(id)})
# 	resp = jsonify('User deleted successfully!')
# 	resp.status_code = 200
# 	return resp
		
# @app.errorhandler(404)
# def not_found(error=None):
#     message = {
#         'status': 404,
#         'message': 'Not Found: ' + request.url,
#     }
#     resp = jsonify(message)
#     resp.status_code = 404

#     return resp

# @app.route('/')
# def base():
#     return Response(response=json.dumps({"Status": "UP"}),
#                     status=200,
#                     mimetype='application/json')


# @app.route('/mongodb', methods=['GET'])
# def mongo_read():
#     data = request.json
#     if data is None or data == {}:
#         return Response(response=json.dumps({"Error": "Please provide connection information"}),
#                         status=400,
#                         mimetype='application/json')
#     obj1 = MongoAPI(data)
#     response = obj1.read()
#     return Response(response=json.dumps(response),
#                     status=200,
#                     mimetype='application/json')


# @app.route('/mongodb', methods=['POST'])
# def mongo_write():
#     data = request.json
#     if data is None or data == {} or 'Document' not in data:
#         return Response(response=json.dumps({"Error": "Please provide connection information"}),
#                         status=400,
#                         mimetype='application/json')
#     obj1 = MongoAPI(data)
#     response = obj1.write(data)
#     return Response(response=json.dumps(response),
#                     status=200,
#                     mimetype='application/json')

# @app.route('/mongodb', methods=['PUT'])
# def mongo_update():
#     data = request.json
#     if data is None or data == {} or 'Filter' not in data:
#         return Response(response=json.dumps({"Error": "Please provide connection information"}),
#                         status=400,
#                         mimetype='application/json')
#     obj1 = MongoAPI(data)
#     response = obj1.update()
#     return Response(response=json.dumps(response),
#                     status=200,
#                     mimetype='application/json')


# @app.route('/mongodb', methods=['DELETE'])
# def mongo_delete():
#     data = request.json
#     if data is None or data == {} or 'Filter' not in data:
#         return Response(response=json.dumps({"Error": "Please provide connection information"}),
#                         status=400,
#                         mimetype='application/json')
#     obj1 = MongoAPI(data)
#     response = obj1.delete(data)
#     return Response(response=json.dumps(response),
#                     status=200,
#                     mimetype='application/json')

if __name__ == "__main__":
    app.run()