from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker

HOST = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = ''
DB = 'DBHOMEWORK'

# dialect + driver://username:passwor@host:port/database
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'

engine = create_engine(DB_URI, echo=False)

Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base(engine)  # SQLORM基类
session = Session()  # 实例化

class Student(Base):
    __tablename__ = 'student'  # 表名
    userName = Column(String(10), primary_key=True, autoincrement=True)
    password = Column(String(10))


Base.metadata.create_all()  # 将模型映射到数据库中
