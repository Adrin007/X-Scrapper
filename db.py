from pymongo import MongoClient
from scrapper import scrapper
import os
from dotenv import load_dotenv
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")
connection = f'mongodb+srv://adrin_sanchez:{DB_PASSWORD}@cluster0.6wwbb.mongodb.net/'
from datetime import datetime, timedelta, timezone
client = MongoClient(connection)
db = client.scrapCollection

def insert():
    try:
        utc_now = datetime.now(timezone.utc)
        ist_now = utc_now + timedelta(hours=5, minutes=30)
        insertion_date = ist_now.strftime("%d-%m-%Y")
        insertion_time = ist_now.strftime("%I:%M %p")
        collection = db.trendScrap
        trends,ip = scrapper()
        data = {
            "trends":trends,
            "insertedDate":insertion_date,
            "insertedTime":insertion_time,
            "ip":ip
        }
        id = collection.insert_one(data).inserted_id
        return id
    except UnboundLocalError:
        print("Unable to Scrap.")
        print("Shutting Down....")

def main():
    insert()
    
if __name__ == "__main__":
    main()