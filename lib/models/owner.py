from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .session import session

class Owner(Base):
    __tablename__="owner"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    
    toys = relationship("Toy", backref="owner")
    
    @classmethod
    def find_or_create_by(cls, email):
        owner = session.query(cls).filter(cls.email.like(email)).first()
        if owner:
            return owner
        else:
            owner = Owner(email=email)
            session.add(owner)
            session.commit()
            return owner
    
        # Query the db for a owner by email
        
    
    def __repr__(self):
        return f"\n<Owner " \
            + f"\n   id={self.id}, " \
            + f"\n   first_name={self.first_name}, " \
            + f"\n   last_name={self.last_name}, " \
            + f"\n   email={self.email}, " \
            + f"\n   phone_number={self.phone_number}, " \
            + f"\n   address={self.address}, " \
            + f"\n   city={self.city}, " \
            + f"\n   state={self.state}, " \
            + f"\n   zip_code={self.zip_code}" \
            + "\n>"