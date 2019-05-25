from sqlalchemy_declarative import Person, Base, Address
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

print(session.query(Person).all())

person = session.query(Person).first()
print(person.name)

print(session.query(Address).filter(Address.person == person).all())

print(session.query(Address).filter(Address.person == person).one())

address = session.query(Address).filter(Address.person == person).one()
print(address.post_code)