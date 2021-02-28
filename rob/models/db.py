import csv 
import pandas as pd 
from sqlalchemy import create_engine
from sqlalchemy import types


def to_sql(df):
    engine = create_engine('sqlite:///app/rob/data/profile.db') # connect to server
    df.to_sql('Table', con=engine, index=False, if_exists='append')
    
if __name__ == '__main__':
    df = pd.read_csv('app/rob/data/mydata.csv', sep=',', quotechar='\'',
                 encoding='utf8')
    to_sql(df)