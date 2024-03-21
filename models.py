from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    status = Column(String(20))
    item = Column(String(20))
