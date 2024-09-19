from fittrack.models import session, User

def get_user_by_id(user_id):
    return session.query(User).filter_by(id=user_id).first()

def get_all_users():
    return session.query(User).all()
