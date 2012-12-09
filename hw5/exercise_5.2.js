#Crunching the Zipcode dataset
#Please download the zips.json dataset and import it into a collection of your choice.
	mongoimport -d m101 -c zips < zips.json

#Please calculate the average population of cities in California (abbreviation CA) and New York (NY) (taken together)
#with populations over 25,000.

#For this problem, assume that a city name that appears in more than one state represents two separate cities.

#Please round the answer to a whole number.
#Hint: The answer for CT and NJ is 49749.

db.zips.aggregate([
	{$match:{$or:[{state:'CA'}, {state:'NY'}]}},
	{$group:{_id:{city:'$city', state:'$state'}, population:{$sum:'$pop'}, zips:{$sum:1}}},
	{$match:{population:{$gt:25000}}},
	{$group:{_id:{}, avg_population:{$avg:'$population'}}}
])
