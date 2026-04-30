import requests
import pandas as pd
from sqlalchemy import create_engine

API_KEY = 'cf64d613c7254c0ebddb2ec61cf92cc4'
engine = create_engine('postgresql://postgres:postgres@localhost:5432/layoff_pipeline')

headers = {'Content-type': 'application/json'}
payload = { "seriesid": ["LNS14000000"], "startyear": "2020", "endyear": "2026",
"registrationkey": API_KEY}

response = requests.post(
    'https://api.bls.gov/publicAPI/v2/timeseries/data/',
    json=payload,
    headers=headers) 
data = response.json() 
print(data['status'])


records = []
for series in data['Results']['series']:
    for item in series['data']:
        if item['value'] != '-':
            records.append({
                'year': item['year'],
                'month': item['period'].replace('M', ''),
                'unemployment_rate': float(item['value'])
            })

df = pd.DataFrame(records)
print(df.head())

df.to_sql('unemployment', engine, schema='staging', if_exists='replace', index=False)
print('BLS data loaded successfully')