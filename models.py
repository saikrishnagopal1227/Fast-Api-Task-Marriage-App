from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    city = Column(String, nullable=False)
    interests = Column(String, nullable=True)  # Store interests as a comma-separated string
