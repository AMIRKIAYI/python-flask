
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Create a new user
user = User(name="Moon lover", age=25)
session.add(user)
session.commit()