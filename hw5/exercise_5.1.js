#Finding the most frequent author of comments on your blog
#In this assignment you will use the aggregation framework to find the most frequent author of comments on your blog. We will be using the same dataset as last week.

#Start by downloading the posts.json dataset from last week's homework, found in hw4-3.tar or hw4-3.zip. Then import into your blog database as follows:

#mongoimport -d blog -c posts --drop < posts.json

#Now use the aggregation framework to calculate the author with the greatest number of comments.

#To help you verify your work before submitting, the author with the least comments is Mariela Sherer and she commented 387 times.

#Ok, please choose your answer below for the most prolific comment author:

db.posts.aggregate([
	{$unwind:'$comments'},
	{$group:{_id:'$comments.author', count:{$sum:1}}},
	{$sort:{count:-1}},
	{$limit:10},
	{$project:{_id:0, author:'$_id', count:1}}
])

