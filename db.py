from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# اتصال به دیتابیس
engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()

# مدل کاربران
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    coins = Column(Integer, default=0)
    grade = Column(String)   # پایه تحصیلی
    major = Column(String)   # رشته تحصیلی
    province = Column(String)  # استان
    city = Column(String)      # شهر

# مدل سوالات (اختیاری برای سوالات مشاوره‌ای)
class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    question_text = Column(String)
    answer_text = Column(String, nullable=True)

# تابع ساخت جداول
def create_tables():
    Base.metadata.create_all(engine)

# تابع گرفتن سشن
def get_session():
    Session = sessionmaker(bind=engine)
    return Session()
