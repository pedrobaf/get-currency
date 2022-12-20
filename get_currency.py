import requests
import os 
import json
import pandas as pd
from dotenv import load_dotenv

load_dotenv() 

API_KEY = os.getenv("API_KEY")
basePath = os.path.dirname(os.path.abspath(__file__))
base = "USD"
symbols = "BRL"

url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base={base}&symbols={symbols}&prettyprint=false&show_alternative=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

with open("res.json", "w") as f:
    f.write(json.dumps(response.json(), indent=4)) 
    
# converting json to csv file
df = pd.read_json ("res.json")
df.to_csv (basePath + "/res.csv", index = None)


