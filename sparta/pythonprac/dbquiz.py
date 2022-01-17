
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


same_star = list(db.movies.find({'star':'9.39'},{'_id':False}))

for star in same_star:
    print(star['title'])