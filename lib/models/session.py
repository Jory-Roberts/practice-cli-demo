from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db/toy_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()