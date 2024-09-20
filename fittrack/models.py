from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    fitness_level = Column(String)

    physical_goals = relationship("PhysicalGoal", back_populates="user")
    workouts = relationship("Workout", back_populates="user")
    nutrition_logs = relationship("NutritionLog", back_populates="user")
    mental_health_logs = relationship("MentalHealthLog", back_populates="user")

class PhysicalGoal(Base):
    __tablename__ = 'physical_goals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    goal = Column(String, nullable=False)

    user = relationship("User", back_populates="physical_goals")  # Add this line

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    exercise = Column(String)
    duration = Column(Integer)  # duration in minutes
    calories_burned = Column(Integer)

    user = relationship("User", back_populates="workouts")

class NutritionLog(Base):
    __tablename__ = 'nutrition_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    meal = Column(String)
    calories = Column(Integer)

    user = relationship("User", back_populates="nutrition_logs")

class MentalHealthLog(Base):
    __tablename__ = 'mental_health_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    entry = Column(String)

    user = relationship("User", back_populates="mental_health_logs")

# Database setup
engine = create_engine('sqlite:///fittrack.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
