import re
import os
from flask import Flask, render_template
from pymongo import MongoClient
from db import insert
from bson.objectid import ObjectId
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter
from dotenv import load_dotenv
import json
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")
app = Flask(__name__)
connection = f'mongodb+srv://adrin_sanchez:{DB_PASSWORD}@cluster0.6wwbb.mongodb.net/'
client = MongoClient(connection)
db = client.scrapCollection

def json_serialize(obj):
    if isinstance(obj, ObjectId):
        return str(obj)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trends', methods=['POST'])
def run_script():
    inserted_id = insert()
    data = db.trendScrap.find_one({"_id": inserted_id})
    trends = data.get('trends', [])
    date = data.get('insertedDate')
    time = data.get('insertedTime')
    ipAddress = data.get('ip')
    prettyData = json.dumps(data,default=json_serialize,ensure_ascii=False,indent=2)
    highlightedData = highlight(prettyData, JsonLexer(), HtmlFormatter(style='monokai', full=True))
    return render_template("trends.html",insertedTrends = trends, insertedDate = date, insertedtime = time, ip = ipAddress, rawData = highlightedData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
