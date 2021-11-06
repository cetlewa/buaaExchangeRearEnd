from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

HOST = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = ''
DB = 'DBHOMEWORK'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8". \
    format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DB)

engine = create_engine(DB_URI, echo=False)

Session = scoped_session(sessionmaker(bind=engine))

session = Session()

Base = declarative_base(engine)



