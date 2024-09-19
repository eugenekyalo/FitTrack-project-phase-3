from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    fitness_level = Column(String)

# Define other models similarly

# Database setup (for app use)
engine = create_engine('sqlite:///fittrack.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
