import os

from sqlalchemy import create_engine
from sqlalchemy import MetaData


user = os.getenv('USER', 'vova')
password = os.getenv('PASSWORD', '123456')
host = os.getenv('HOST', '127.0.0.1')
port = os.getenv('PORT', '5432')
database = os.getenv('DATABASE', 'issues_db')

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

metadata = MetaData()
