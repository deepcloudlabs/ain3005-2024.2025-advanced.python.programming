from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017')
hsbc = mongo_client['hsbc']
accounts_collection = hsbc['accounts']

result = accounts_collection.delete_many(
    {"status": {"$in": ["BLOCKED", "CLOSED"]}}
)

print(f"{result.deleted_count} documents removed!")
