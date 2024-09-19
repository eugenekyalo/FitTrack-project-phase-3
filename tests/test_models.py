import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fittrack.models import Base, User

@pytest.fixture(scope='module')
def test_db():
    # Set up an in-memory database for testing
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session  # Provide the fixture value
    
    Base.metadata.drop_all(engine)
    session.close()

def test_create_user_model(test_db):
    session = test_db
    user = User(name='Jane Doe', age=25, height=165, weight=60, fitness_level='Beginner')
    session.add(user)
    session.commit()
    
    assert session.query(User).filter_by(name='Jane Doe').first() is not None
