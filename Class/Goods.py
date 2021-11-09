from sqlalchemy import Column, Integer, String, VARCHAR

from Class.Father import Father


class Goods(Father):
    __tablename__ = "Goods"
    goodId = Column(Integer, primary_key=True, autoincrement=True)  # 默认不可为空
    goodName = Column(VARCHAR(50))
    sellerId = Column(Integer)
    goodType = Column(VARCHAR(50))
    goodPrice = Column(Integer)
    goodDescription = Column(VARCHAR(100))
    goodLike = Column(Integer)
    goodDislike = Column(Integer)
