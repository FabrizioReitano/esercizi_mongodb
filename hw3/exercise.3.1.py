# Write a program in the language of your choice that will remove the
# lowest homework score for each student. Since there is a single document
# for each student containing an array of scores, you will need to update
# the scores array and remove the homework.

import pymongo
import sys

# connnessione al db
connection = pymongo.Connection("mongodb://localhost", safe=True)

#specifica il db da usare
db = connection.school
students = db.students

try:
	cursor = students.find()
	#cursor = cursor.limit(1)
	tot = 0
	for student in cursor:
		lowest_score = 200
		for score in student['scores']:
			#print "nome:",student['name'], "voto: ", score
			if(score['type'] == 'homework' and score['score'] < lowest_score):
				#print "basso: ",score['score']
				lowest_score = score['score']
				lowest_score_item = score
		# rimuove il voto 'homework' piu' basso
		student['scores'].remove(lowest_score_item)
		#print "voti: ", student['scores']
		# rimpiazza la vecchia lista di voti con la nuova
		students.update({'_id':student['_id']}, {'$set':{'scores':student['scores']}})

except:
    print "Error trying to read collection:", sys.exc_info()