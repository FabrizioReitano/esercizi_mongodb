import pymongo

from pymongo import Connection
connection = Connection('localhost', 27017)

db = connection.questionariDB

question = db.question.find_one()

print question['text']