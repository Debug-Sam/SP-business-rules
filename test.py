import pandas as pd
from sqlalchemy import create_engine
from _functions.config import config

db = config()

# choose the database to use
port = 5432

# construct an engine connection string
engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
    user = db['user'],
    password = db['password'],
    host = db['host'],
    port = 5432,
    database = db['database'],
)

# create sqlalchemy engine
engine = create_engine(engine_string)

# read a table from database into pandas dataframe, replace "tablename" with your table name
column_names = ['idproducts', 'name', 'brand', 'category']
df = pd.read_sql_table(table_name='products', con=engine, columns=column_names)

print(df)