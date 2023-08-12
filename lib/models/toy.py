from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .base import Base

class Toy(Base):
    __tablename__="toy"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    type = Column(String, nullable=False)
    location = Column(String)
    notes = Column(String)
    is_favorite = Column(Boolean, default=False)
    
    owner_id = Column(Integer, ForeignKey("owner.id"))
    
    def __repr__(self):
        return f"\n<Toy " \
            + f"\n   id={self.id}, " \
            + f"\n   name={self.name}, " \
            + f"\n   manufacturer={self.manufacturer}, " \
            + f"\n   type={self.type}, " \
            + f"\n   location={self.location}, " \
            + f"\n   notes={self.notes}, " \
            + f"\n   is_favorite={self.is_favorite}" \
            + "\n>"