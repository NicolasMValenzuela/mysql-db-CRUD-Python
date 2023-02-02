from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:123456789@localhost/hola_mundo')
Session = sessionmaker(bind=engine)
Session = Session()

Base = declarative_base()