# Get Currency

Sign up to `<https://openexchangerates.org/>` so you can get your APP ID.

It is a goog idea to go to the ENDPOINTS and read the examples

## To hide your API KEYS

Create a archive .env (see get_currency.py).

## To create a virtual environment
In your prmpt:

```python
python -m venv venv
```
## Start the virtual evironment

```for windows
source venv/Script/activate
```

```python
pip install python-dotenv
```

### Do not forget to install all the instances you are importing in the virtual environment.

# Explaining the code:
```python
import requests
import os 
import json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
```
First, I imported all the libraries I was going to use. 

```python
# Here is the variable for the API Key created at .env
API_KEY = os.getenv("API_KEY")
# Here I created a variable to hide the file path
basePath = os.path.dirname(os.path.abspath(__file__))

base = "USD"
# Here I am converting Dollars to Brazilian Reais. Check the documentation to see what kind of rates you would need.
symbols = "BRL"

url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base={base}&symbols={symbols}&prettyprint=false&show_alternative=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
```
Then, I created variables to query the API

```python
with open(basePath + "/res.json", "w") as f:
    f.write(json.dumps(response.json(), indent=4))

```
Afterwards, I created a json file to display the response.

```python
# converting json to csv file
df = pd.read_json ("res.json")
df.to_csv (basePath + "/res.csv", index = None)
```

Lastly, I converted the json file to csv.
