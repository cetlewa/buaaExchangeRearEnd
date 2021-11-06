from sqlalchemy import Column, Integer, String, VARCHAR

from Class.Father import Father


class User(Father):
    __tablename__ = "User"
    userID = Column(Integer, primary_key=True, autoincrement=True)  # 默认不可为空
    userName = Column(VARCHAR(50))
    password = Column(VARCHAR(50))
    gender = Column(VARCHAR(5))
    grade = Column(VARCHAR(10))
    tel = Column(VARCHAR(20), nullable=True)
    district = Column(VARCHAR(300), nullable=True)
