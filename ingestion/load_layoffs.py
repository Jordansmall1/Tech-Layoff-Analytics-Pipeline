import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/layoff_pipeline')
df = pd.read_csv('/Users/clerancesmal/Documents/layoff_pipeline/Data/layoffs.csv')
print(df.shape)
print(df.head())

df.to_sql('layoffs', engine, schema='staging', if_exists='replace', index=False)
print('Data loaded successfully')

#look at data closer#
#print(df.dtypes)#