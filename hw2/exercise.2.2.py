#Write a program in the language of your choice that will remove the lowest 
#homework score for each student from the dataset that you imported in HW 2.1. 
#Since each document is one score, it should remove one document per student. 

import pymongo
import sys

# connnessione al db
connection = pymongo.Connection("mongodb://localhost", safe=True)

#specifica il db da usare
db = connection.students
grades = db.grades

try:
	cursor = grades.find({'type':'homework'})
	cursor = cursor.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])
	#cursor = cursor.limit(20)
	current_student_id = -1
	tot = 0
	for item in cursor:
		if current_student_id != item['student_id'] :
			current_student_id = item['student_id']
			grades.remove({'_id' : item['_id']})
			tot = tot + 1
			print "Eliminato: ", item['_id']

except:
    print "Error trying to read collection:", sys.exc_info()[0]

print "totale eliminati: ", tot
