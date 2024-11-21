from pymongo import MongoClient

accounts = [
    {"iban": "BE38548738513272", "balance": 1_000_000, "status": "ACTIVE"},
    {"iban": "BE94897142923114", "balance": 2_000_000, "status": "CLOSED"},
    {"iban": "BE74817623593107", "balance": 3_000_000, "status": "BLOCKED"},
    {"iban": "BE86812627195350", "balance": 4_000_000, "status": "ACTIVE"},
    {"iban": "BE58957532365179", "balance": 5_000_000, "status": "CLOSED"},
    {"iban": "BE53978452488353", "balance": 6_000_000, "status": "BLOCKED"}
]
mongo_client = MongoClient('mongodb://localhost:27017')
hsbc = mongo_client['hsbc']
accounts_collection = hsbc['accounts']
with mongo_client.start_session() as ses:
    def insert_all_accounts(s):
        global accounts
        global accounts_collection
        for account in accounts:
            accounts_collection.insert_one(account, session=s)
    ses.with_transaction(insert_all_accounts)
