#Find all exam scores greater than or equal to 65. and sort those scores from lowest to highest. 

db.grades.find({type : 'exam', score : {$gte : 65}}).sort({score : 1})

#What is the student_id of the lowest exam score above 65?

22