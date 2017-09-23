from sqlalchemy import Column, ForeignKey, Integer, String,DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import  create_engine
import datetime

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key = True)
    title = Column(String(100), nullable = False, index = True)
    price = Column(Integer, nullable = True)
    tb_id = Column(Integer, nullable=False)
    pic = Column(String(200),nullable = True)
    brand = Column(String(20), ForeignKey("brand.name"), nullable=True)
    sell_info=relationship("Sell_info")
    Brand = relationship("Brand")


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer,primary_key=True)
    tb_sid = Column(Integer, nullable = False, index = False)
    name = Column(String(20), nullable = False, index = True)
    url = Column(String(20), nullable=True, index=False)
    sell_info = relationship("Sell_info")
    brand = Column(String(20), ForeignKey("brand.name"), nullable=True)
    Brand = relationship("Brand")


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer,primary_key=True)
    name = Column(String(20), nullable = False, index = True)
    name2 = Column(String(20), nullable=True, index=True)
    logo = Column(String(20), nullable=True, index=False)
    Item = relationship("Item")


class Sell_info(Base):
    __tablename__ = 'sell_info'
    id = Column(Integer,primary_key=True)
    date = Column(DATE, default=datetime.datetime.now())
    price = Column(Integer, nullable=False, index=True)
    tb_id = Column(Integer, ForeignKey("item.tb_id"), nullable=True)
    tb_sid = Column(Integer, ForeignKey("shop.tb_sid"), nullable=True)
    recom = Column(Integer, nullable=True, index=True)
    Item = relationship("Item")
    Shop = relationship("Shop")


engine = create_engine('sqlite:///item.db')

Base.metadata.create_all(engine)