import os
from dotenv import  load_dotenv
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


load_dotenv()
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
user = os.getenv("user")
pswd = os.getenv("password")


Base = declarative_base()
engine = create_engine(f"postgresql://{user}:{pswd}@194.67.203.117:5437/trainingTest")


class User(Base):
    __tablename__ = 'user_data'
    __table_args__ = {"schema": "lixakov"}

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    middle_name = Column(String(250))
    bornData = Column(Date)
    gender = Column(String(250))


class User_data(Base):
    __tablename__ = 'user_data_meta'
    __table_args__ = {"schema": "lixakov"}

    id = Column(Integer, primary_key=True)
    citizenship = Column(String(250))
    comment = Column(String(250))
    education = Column(String(250))
    phone = Column(String(250))
    user_id = Column(Integer, ForeignKey(User.id))

