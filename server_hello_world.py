import bottle
import pymongo

@bottle.route('/')
def index():
	from pymongo import Connection
	connection = Connection('localhost', 27017)
	db = connection.questionariDB
	question = db.question.find_one()
	string = question.text
	return  string
	
bottle.run(host='localhost', port=8080)