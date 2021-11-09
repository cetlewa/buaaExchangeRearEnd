from sqlalchemy import Column, Integer, String, VARCHAR

from Class.Father import Father


class GoodsPicture(Father):
    __tablename__ = "GoodsPicture"
    picId = Column(Integer, primary_key=True, autoincrement=True)  # 默认不可为空
    goodId = Column(Integer)
    picUrl = Column(VARCHAR(100))
