from models import Owner, Toy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/toy_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

import random
from faker import Faker

fake = Faker()

state_abbreviations = [
    "CA",
    "NY",
    "TX",
    "FL",
    "IL",
    "PA",
    "OH",
    "GA",
    "MI",
    "WA",
    "NC",
    "NJ",
    "VA",
    "AZ",
    "MA",
    "TN",
    "IN",
    "MO",
    "MD",
    "WI",
]

toy_types = [
    "Action Figures",
    "Dolls",
    "Board Games",
    "Puzzles",
    "Remote-Controlled Vehicles",
    "Building Blocks",
    "Stuffed Animals",
    "Arts and Crafts Kits",
    "Educational Toys",
    "Outdoor Playsets",
    "Pretend Play Sets",
    "Vehicles and Playsets",
    "Musical Instruments",
    "Electronic Toys",
    "Sports Equipment",
    "Science Kits",
    "Construction Sets",
    "Robotics Kits",
    "Collectible Toys",
    "Dress-Up Accessories"
]

toy_locations = [
    "Andy's Room",
    "Pizza Planet",
    "Sunnyside Daycare",
    "Al's Toy Barn",
    "Toy Story Midway Mania!",
    "Bonnie's House",
    "RC Raceway",
    "Star Command Spaceship",
    "Andy's Toy Box",
    "Molly's Room",
    "Big Al's Toy Barn",
    "Poultry Palace",
    "Ken's Dream House",
    "The Claw Machine",
    "Trixie's Playground",
    "Hawaiian Vacation Playset",
    "Bonnie's Closet",
    "Chatter Telephone's Corner",
    "Buster's Doghouse",
    "Carnival Playland"
]

session.query(Owner).delete()
session.query(Toy).delete()

for _ in range(10):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name}_{last_name}@gmail.com"
    owner = Owner(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=fake.phone_number(),
        address=fake.street_address(),
        city=fake.city(),
        state=random.sample(state_abbreviations, 1)[0],
        zip_code=fake.postcode(),
    )
    
    for _ in range(5):
        
        toy = Toy(
            name=fake.first_name(),
            manufacturer=fake.company(),
            type=random.sample(toy_types, 1)[0],
            location=random.sample(toy_locations, 1)[0],
            notes=fake.paragraph(nb_sentences=2)
        )
        
        owner.toys.append(toy)
        
        session.add(owner)
        session.commit()

import ipdb

ipdb.set_trace()
