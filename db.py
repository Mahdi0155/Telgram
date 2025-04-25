from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# اتصال به دیتابیس SQLite
engine = create_engine('sqlite:///data.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# جدول کاربران
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)  # آیدی تلگرام کاربر
    username = Column(String)
    coins = Column(Integer, default=0)
    grade = Column(String, default="")
    major = Column(String, default="")
    province = Column(String, default="")
    city = Column(String, default="")

# ساخت جدول‌ها
def create_tables():
    Base.metadata.create_all(engine)
